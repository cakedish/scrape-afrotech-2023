"""
Determine the lowest access type value from a list of access types
"""

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
