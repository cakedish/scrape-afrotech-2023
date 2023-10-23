"""
Determine the lowest access type value from a list of access types
"""
import cleanup_access_types

# Define a dictionary to map access type names to their values
access_type_levels = {
    "General Admission": 1,
    "Students": 2,
    "Executive": 3,
    "All Access": 4,
    "Speakers": 5,
    "Corporate": 6,
    "Sponsors": 7,
    "Press": 8,
    "RSVP Required": 9,
    "Add-On": 10,
}


def this(access_types):
    """
    Determine the lowest access type value from a list of access types
    """
    # Initialize the lowest value with a large number
    low = float("inf")

    # Iterate through the access types and find the lowest value
    for access_type in access_types:
        value = access_type_levels.get(access_type)
        if value is not None and value < low:
            low = value

    return low


# Test the function
if __name__ == "__main__":
    # Example usage:
    access_types_list = ["Students", "Executive", "Speakers"]
    lowest_value = this(access_types_list)
    print("Lowest Value:", lowest_value)

    event_data = [
        {"access": ["Students", "Student"]},
        {"access": ["Speakers", "Speakers & All Access Registration"]},
        {
            "access": [
                "All Access Badge Holders",
                "All Access",
                "All Access Ticket Holders",
            ]
        },
        {"access": ["Corporate", "Corporate Sponsors"]},
        {"access": ["Executive", "Exec"]},
        {"access": ["RSVP Only", "Invite Only", "RSVP Required", "RSVP Requirfed"]},
        {"access": ["GA"]},
        {"access": ["Press"]},
        {"access": ["Sponsors"]},
        {"access": ["Add-On for all Others"]},
    ]

    access_type_strings = {v: k for k, v in access_type_levels.items()}

    # Iterate through the list of event objects and print lowest access level
    for event in event_data:
        print("IN : ", event["access"])
        level = this(cleanup_access_types.this(event["access"]))
        print(f"OUT: {level} -> {access_type_strings[level]}")
