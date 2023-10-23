# Access Levels
1. Students
2. Speakers
3. All Access
4. Corporate
5. Sponsors
6. Executive
7. RSVP
8. GA
9. Press
10. Add-On

```html
<option value="1">General Admission</option>
<option value="2">Students</option>
<option value="3">Executive</option>
<option value="4">All Access</option>
<option value="5">Speakers</option>
<option value="6">Corporate</option>
<option value="7">Sponsors</option>
<option value="8">Press</option>
<option value="9">RSVP Required</option>
<option value="10">Add-On</option>
```

```python
# Test the function
import cleanup_access_types

if __name__ == "__main__":
    # Example usage:
    access_types_list = ["Students", "Executive", "Speakers"]
    lowest_value = this(access_types_list)
    print("Lowest Value:", lowest_value)

    event_data = [
        {"access": ["Students", "Executive", "Speakers"]},
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
```