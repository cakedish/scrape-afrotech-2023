import re
import html

def this(description: str, event_id = 0) -> str:
    """Sanitize the description for an event"""

    # Escape HTML entities
    escaped_description = html.escape(description)
    sanitized_description = f'{escaped_description}'
    
    return sanitized_description




# Test the function
if __name__ == "__main__":

    description = "<script>alert('Hello World');</script>"
    print("Before sanitization: {0}".format(description))
    print("After sanitization: {0}".format(this(description)))

    description = "<p>Here is a paragraph</p>"
    print("Before sanitization: {0}".format(description))
    print("After sanitization: {0}".format(this(description)))

    # Create a test case with a description that contains a single quote
    description = "<p>Here's a paragraph</p>"
    print("Before sanitization: {0}".format(description))
    print("After sanitization: {0}".format(this(description)))

    # Create a test case with a multi-line description
    description = """Experience an evening of inspiration and networking 
            while celebrating the achievements of remarkable leaders at the 
            Women of Influence Reception, Presented by Viarae.  
            This event is Invite Only."""
    print("Before sanitization: {0}".format(description))
    print("After sanitization: {0}".format(this(description)))


    description = """
    Brunch your way through Austin, celebrating and supporting the city's diverse and delicious brunch culture before departing from an amazing AFROTECH™ week. See below for locations and some special offerings:

    Anthem
    Hours: 11 AM - 10 PM
    Distance: 0.5 miles | 12 mins walk
    Special: Free order of Thai Doughnuts with 3 or more guests (6 pieces per order). Contains gluten and dairy, nut-free, vegetarian.

    P6 Lounge Bar
    Hours: 10 AM - 4 PM
    Distance: 0.4 miles | 10 mins walk
    Special: Agreed to provide a 10% discount (excluding alcohol) to attendees who show AfroTech badge.
    """
    print("Before sanitization: {0}".format(description))
    print("After sanitization: {0}".format(this(description)))
