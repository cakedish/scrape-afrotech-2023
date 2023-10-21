from bs4 import BeautifulSoup
from datetime import datetime
import convert_to_iso8601
import cleanup_access_types
import sanitize_description

import os
import json
import bios

# Directory where HTML files are stored
html_directory = './downloads/'

# Create a list and a dictionay to store events
events_list = []
events_dict = {}

# Iterate through the HTML files in the directory
for filename in os.listdir(html_directory):
    if filename.endswith(".html"):
        # Initialize a dictionary to store metadata
        metadata_dict = {}

        # Split the filename by '_' and get the second part
        # Remove the '.html' extension
        event_id = filename.split('_')[1].replace('.html', '')
        metadata_dict['id'] = event_id

        print(f"Processing event {event_id}")

        file_path = os.path.join(html_directory, filename)
        
        try:
            # Read the HTML content from the file
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract elements from the HTML content
            event_name = soup.find('h1', class_='ev-name event').text.strip()
            
            # Check if a title was found
            if event_name:
                # If a description is found, sanitize it
                metadata_dict['title'] = sanitize_description.this(event_name)
            else:
                # If no title is found, provide a default
                metadata_dict['title'] = "No title available"

            # <div class="ev-description">
            event_description = soup.find('div', class_='ev-description').text.strip()

            # Check if a description was found
            if event_description:
                # If a description is found, sanitize it
                metadata_dict['description'] = sanitize_description.this(event_description)
            else:
                # If no description is found, provide a default 
                metadata_dict['description'] = "No description available"


            # Find all metadata elements
            metadata_elements = soup.find_all('div', class_='ev-metadata')

            # Loop through metadata elements
            for metadata_element in metadata_elements:
                key_element = metadata_element.find('strong')
                
                if key_element:
                    key = key_element.text.strip()
                    value = metadata_element.text.strip()
                    value = value.replace(key, "").strip()

                    if key == "ACCESS":
                        value = value.split(',')
                        value = [v.strip() for v in value]
                        value = cleanup_access_types.this(value)
                    else:
                        value = value.replace('\n', ' ').strip()

                    # convert DATE from MM/DD/YYYY to YYYY-MM-DD
                    if key == "DATE":
                        date_obj = datetime.strptime(value, "%m/%d/%Y")
                        value = datetime.strptime(value, "%m/%d/%Y").strftime("%Y-%m-%d")

                elif metadata_element.find('a'):
                    # Metadata element with an anchor (<a>) element
                    key = "link"
                    value = metadata_element.find('a')['href'].strip()
                    
                elif metadata_element.find('img'):
                    # Metadata element with an image (<img>) element
                    key = "image"
                    value = metadata_element.find('img')['src'].strip()

                metadata_dict[key.lower()] = value

            # convert the date and time keys to ISO 8601 format
            metadata_dict["start"], metadata_dict["end"] = convert_to_iso8601.this(metadata_dict["date"], metadata_dict["time"])

            events_list.append(metadata_dict)
            events_dict[event_id] = metadata_dict      

        except Exception as e:
            print(f"Error processing content from {filename}, Error: {str(e)}")

# TODO: color events by access type
# TODO: filter calendar by access type

bios.write('events_list.json', events_list)
bios.write('events_dict.json', events_dict)
