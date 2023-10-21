import os
import bios
from jinja2 import Environment, FileSystemLoader

# define the output directory
output_directory = "./public"

# Read data from the JSON file using the 'bios' module
events = bios.read('events_list.json')

# Create a Jinja2 environment with the templates directory
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('index.html')

# Render the template with the 'events' variable
rendered_template = template.render(events=events)

# Check if the directory exists
if not os.path.exists(output_directory):
    # If it doesn't exist, create the directory
    os.makedirs(output_directory)
    print(f"Directory '{output_directory}' created.")
else:
    print(f"Directory '{output_directory}' already exists.")

# Save the rendered template as an HTML file
with open('public/index.html', 'w') as html_file:
    html_file.write(rendered_template)

print('Template populated with events data and saved as index.html')
