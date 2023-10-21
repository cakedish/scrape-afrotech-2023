from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os

import requests
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of the webpage you want to scrape
url = 'https://experience.afrotech.com/afrotech-schedule/'

# Load the webpage
driver.get(url)

# Wait for the page to load (you may need to adjust the wait time)
driver.implicitly_wait(10)  # Wait for up to 10 seconds for the page to load

print(driver.title)

# Find all anchor elements on the page and extract their href attributes
links = [a.get_attribute('href') for a in driver.find_elements(By.TAG_NAME, 'a')]

# Filter and print links that contain the event ID
filtered_links = []
string_to_match = "event-detail/?conference_id=4246&event_id="
for link in links:
    if string_to_match in link:
        filtered_links.append(link)

# Close the browser
driver.close()

# Specify a directory to save the HTML files
output_directory = "./downloads/"

# Check if the directory exists
if not os.path.exists(output_directory):
    # If it doesn't exist, create the directory
    os.makedirs(output_directory)
    print(f"Directory '{output_directory}' created.")
else:
    print(f"Directory '{output_directory}' already exists.")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Iterate through the filtered links and download the HTML content
for link in filtered_links:
    # Extract a unique identifier for the file name (e.g., event_id)
    unique_identifier = link.split("event_id=")[-1]

    # Generate a file name based on the unique identifier
    file_name = f"event_{unique_identifier}.html"

    # Create the complete file path
    file_path = output_directory + file_name

    try:
        # Send a GET request to the link to fetch the HTML content
        response = requests.get(link, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the HTML content to a file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Downloaded: {link}")
        else:
            print(f"Failed to download: {link}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading: {link}, Error: {str(e)}")
