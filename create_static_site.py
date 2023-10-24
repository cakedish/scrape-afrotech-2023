"""Compiles the metadata and template into a static HTML file"""
import os
import json
import bios
from jinja2 import Environment, FileSystemLoader

# Define the output directory
PUBLIC_DIRECTORY = "./public"

# Read data from the JSON file using the 'bios' module
events = bios.read("events_list.json")

# Create a Jinja2 environment with the templates directory
env = Environment(loader=FileSystemLoader("templates"))

# Load the template for event processing
event_template = env.get_template("index.html")

# Process each event and store them in a list
processed_events = []
for event in events:
    # Apply Jinja template-like processing to each event
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
        if event.get("image"):
            processed_event["extendedProps"]["image"] = event["image"]

    if event.get("link"):
        processed_event["extendedProps"]["link"] = event["link"]



    processed_events.append(processed_event)

# Render the template with the processed events
rendered_template = event_template.render(events=json.dumps(processed_events))

# Check if the directory exists
if not os.path.exists(PUBLIC_DIRECTORY):
    # If it doesn't exist, create the directory
    os.makedirs(PUBLIC_DIRECTORY)
    print(f"Directory '{PUBLIC_DIRECTORY}' created.")
else:
    print(f"Directory '{PUBLIC_DIRECTORY}' already exists.")

# Save the rendered template as an HTML file
with open(f"{PUBLIC_DIRECTORY}/index.html", "w", encoding="utf-8") as html_file:
    html_file.write(rendered_template)

print(f"Template populated with events data and saved as {PUBLIC_DIRECTORY}/index.html")
