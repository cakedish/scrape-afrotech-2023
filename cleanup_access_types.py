# Define a mapping of access types to groups:
# - Students
# - Speakers
# - All Access
# - Corporate
# - Sponsors
# - Executive
# - RSVP
# - GA
# - Press
# - Add-On

access_type_mapping = {
    "Students": "Students",
    "Student": "Students",
    "Speakers": "Speakers",
    "Speakers & All Access": "All Access",
    "Speakers & All Access Registration": "All Access",
    "All Access Badge Holders": "All Access",
    "All Access": "All Access",
    "All Access Ticket Holders": "All Access",
    "Corporate": "Corporate",
    "Corporate Sponsors": "Sponsors",
    "Executive": "Executive",
    "Exec": "Executive",
    "RSVP Only": "RSVP Required",
    "Invite Only": "RSVP Required",
    "RSVP Required": "RSVP Required",
    "RSVP Requirfed": "RSVP Required",
    "GA": "General Admission",
    "Press": "Press",
    "Sponsors": "Sponsors",
    "Add-On for all Others": "Add-On"
}

def this(access_types: list[str]) -> list[str]:
    """Convert a list of access types to a list of groups."""
    # Create a list to store the mapped groups
    mapped_groups_set = set()

    # Iterate through the provided access types and map them to groups
    for access_type in access_types:
        group = access_type_mapping.get(access_type, "Uncategorized")
        mapped_groups_set.add(group)

    # Convert the set back to a list to maintain order
    mapped_groups_list = list(mapped_groups_set)

    return mapped_groups_list


# Test the function
if __name__ == "__main__":
    event_data = [
        {"access": ["Students", "Student"]},
        {"access": ["Speakers", "Speakers & All Access Registration"]},
        {"access": ["All Access Badge Holders", "All Access", "All Access Ticket Holders"]},
        {"access": ["Corporate", "Corporate Sponsors"]},
        {"access": ["Executive", "Exec"]},
        {"access": ["RSVP Only", "Invite Only", "RSVP Required", "RSVP Requirfed"]},
        {"access": ["GA"]},
        {"access": ["Press"]},
        {"access": ["Sponsors"]},
        {"access": ["Add-On for all Others"]}
    ]

    # Iterate through the list of event objects and organize access types into groups
    for event in event_data:
        if "access" in event:
            print("Before: ", event["access"])
            mapped_groups = this(event["access"])
            print("After : ", mapped_groups)
