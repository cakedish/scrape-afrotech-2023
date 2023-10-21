"""Download metadata from the target site"""
import os

import requests
from requests.exceptions import RequestException

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# Load the webpage
driver.get("https://experience.afrotech.com/afrotech-schedule/")

# Wait for the page to load (you may need to adjust the wait time)
driver.implicitly_wait(10)  # Wait for up to 10 seconds for the page to load

print(driver.title)

# Find all anchor elements on the page and extract their href attributes
links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a")]

# Filter and print links that contain the event ID
filtered_links = []
STRING_TO_MATCH = "event-detail/?conference_id=4246&event_id="
for link in links:
    if STRING_TO_MATCH in link:
        filtered_links.append(link)

# Close the browser
driver.close()

# Specify a directory to save the HTML files
DOWNLOAD_DIRECTORY = "./downloads/"

# Check if the directory exists
if not os.path.exists(DOWNLOAD_DIRECTORY):
    # If it doesn't exist, create the directory
    os.makedirs(DOWNLOAD_DIRECTORY)
    print(f"Directory '{DOWNLOAD_DIRECTORY}' created.")
else:
    print(f"Directory '{DOWNLOAD_DIRECTORY}' already exists.")

headers = {
    # pylint: disable=line-too-long
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Iterate through the filtered links and download the HTML content
for link in filtered_links:
    # Extract a unique identifier for the file name (e.g., event_id)
    unique_identifier = link.split("event_id=")[-1]

    # Generate a file name based on the unique identifier
    file_name = f"event_{unique_identifier}.html"

    # Create the complete file path
    file_path = DOWNLOAD_DIRECTORY + file_name

    try:
        # Send a GET request to the link to fetch the HTML content
        response = requests.get(link, headers=headers, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the HTML content to a file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Downloaded: {link}")
        else:
            print(f"Failed to download: {link}, Status Code: {response.status_code}")
    except RequestException as e:
        print(f"Error downloading: {link}, Error: {str(e)}")
