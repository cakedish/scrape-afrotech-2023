"""Compiles the metadata and template into a static HTML file"""
import os
import bios
from jinja2 import Environment, FileSystemLoader

# Define the output directory
PUBLIC_DIRECTORY = "./public"

# Read data from the JSON file using the 'bios' module
events = bios.read("events.json")

# Create a Jinja2 environment with the templates directory
env = Environment(loader=FileSystemLoader("templates"))

# Load the template for event processing
event_template = env.get_template("index.html.jinja")

# Render the template with the  events; '| tojson' is applied in the template
rendered_template = event_template.render(events=events)

# Check if the directory exists
if not os.path.exists(PUBLIC_DIRECTORY):
    # If it doesn't exist, create the directory
    os.makedirs(PUBLIC_DIRECTORY)

# Save the rendered template as an HTML file
with open(f"{PUBLIC_DIRECTORY}/index.html", "w", encoding="utf-8") as html_file:
    html_file.write(rendered_template)

bios.write(f"{PUBLIC_DIRECTORY}/events.json", events)

print(f"Template populated and saved as {PUBLIC_DIRECTORY}/index.html")
