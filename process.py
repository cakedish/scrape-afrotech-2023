"""Process metadata into JSON"""
import os
from datetime import datetime

import bios
from bs4 import BeautifulSoup

import convert_to_iso8601
import cleanup_access_types
import sanitize_description
import determine_lowest_access


# Directory where HTML files are stored
HTML_DIRECTORY = "./downloads/"

# Create a list and a dictionay to store events
events = []

# Iterate through the HTML files in the directory
for filename in os.listdir(HTML_DIRECTORY):
    if filename.endswith(".html"):
        # Initialize a dictionary to store metadata
        metadata_dict = {}

        # Split the filename by '_' and get the second part
        # Remove the '.html' extension
        event_id = filename.split("_")[1].replace(".html", "")
        metadata_dict["id"] = event_id

        print(f"Processing event {event_id}")

        file_path = os.path.join(HTML_DIRECTORY, filename)

        try:
            # Read the HTML content from the file
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # Extract elements from the HTML content
            event_name = soup.find("h1", class_="ev-name event").text.strip()

            # Check if a title was found
            if event_name:
                # If a description is found, sanitize it
                metadata_dict["title"] = sanitize_description.this(event_name)
            else:
                # If no title is found, provide a default
                metadata_dict["title"] = "No title available"

            # <div class="ev-description">
            event_description = soup.find("div", class_="ev-description").text.strip()

            # Check if a description was found
            if event_description:
                # If a description is found, sanitize it
                metadata_dict["description"] = sanitize_description.this(
                    event_description
                )
            else:
                # If no description is found, provide a default
                metadata_dict["description"] = "No description available"

            # Find all metadata elements
            metadata_elements = soup.find_all("div", class_="ev-metadata")

            # Loop through metadata elements
            for metadata_element in metadata_elements:
                key_element = metadata_element.find("strong")

                if key_element:
                    KEY = key_element.text.strip()
                    value = metadata_element.text.strip()
                    value = value.replace(KEY, "").strip()

                    if KEY == "ACCESS":
                        value = value.split(",")
                        value = [v.strip() for v in value]
                        value = cleanup_access_types.this(value)

                    else:
                        value = value.replace("\n", " ").strip()

                    # convert DATE from MM/DD/YYYY to YYYY-MM-DD
                    if KEY == "DATE":
                        date_obj = datetime.strptime(value, "%m/%d/%Y")
                        value = datetime.strptime(value, "%m/%d/%Y").strftime(
                            "%Y-%m-%d"
                        )

                elif metadata_element.find("a"):
                    # Metadata element with an anchor (<a>) element
                    KEY = "link"
                    value = metadata_element.find("a")["href"].strip()

                elif metadata_element.find("img"):
                    # Metadata element with an image (<img>) element
                    KEY = "image"
                    value = metadata_element.find("img")["src"].strip()

                metadata_dict[KEY.lower()] = value

            # get the access level
            if "access" in metadata_dict:
                metadata_dict["access_id"] = determine_lowest_access.this(
                    metadata_dict["access"]
                )

            # convert the date and time keys to ISO 8601 format
            metadata_dict["start"], metadata_dict["end"] = convert_to_iso8601.this(
                metadata_dict["date"], metadata_dict["time"]
            )

            events.append(metadata_dict)

        except (AttributeError, FileNotFoundError) as e:
            print(f"Error processing content from {filename}, Error: {str(e)}")

# Process each event and store them in a list
processed_events = []

for event in events:
    processed_event = {
        "id": event["id"],
        "title": event["title"],
        "start": event["start"],
        "end": event["end"],
        "extendedProps": {
            "description": event["description"],
            "date": event["date"],
            "time": event["time"],
        },
    }

    if event.get("image"):
        processed_event["extendedProps"]["image"] = event["image"]

    if event.get("link"):
        processed_event["extendedProps"]["link"] = event["link"]

    if event.get("location"):
        processed_event["extendedProps"]["location"] = event["location"]

    if event.get("access"):
        processed_event["extendedProps"]["access"] = event["access"]

        if "General Admission" in event["access"]:
            processed_event["backgroundColor"] = "#4CAF50"
        elif "Students" in event["access"]:
            processed_event["backgroundColor"] = "orange"
        elif "RSVP Required" in event["access"]:
            processed_event["backgroundColor"] = "#F44336"
        elif "All Access" in event["access"]:
            processed_event["backgroundColor"] = "#FFD700"
        else:
            processed_event["backgroundColor"] = "#2196F3"

    processed_events.append(processed_event)

bios.write("events.json", processed_events)
