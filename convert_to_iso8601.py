from datetime import datetime
import re

def this(date_string, time_string):
    # Regular expression pattern to match the start time, end time, and timezone
    pattern = r'(\d{1,2}:\d{2}[ap]m) - (\d{1,2}:\d{2}[ap]m) ([A-Z]{3,4})'

    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")

    # Extract start time, end time, and timezone from the value
    match = re.search(pattern, time_string)

    if match:
        start_time = match.group(1)
        end_time = match.group(2)
        
        # Convert start and end time strings to datetime objects
        start_time_obj = datetime.strptime(start_time, "%I:%M%p")
        end_time_obj = datetime.strptime(end_time, "%I:%M%p")

        # Combine the date and time components
        start_datetime = date_obj.replace(
            hour=start_time_obj.hour, minute=start_time_obj.minute, second=0
        )

        end_datetime = date_obj.replace(
            hour=end_time_obj.hour, minute=end_time_obj.minute, second=0
        )

        # Format the combined datetime objects as ISO 8601 strings
        start_iso8601 = start_datetime.isoformat()
        end_iso8601 = end_datetime.isoformat()

        return start_iso8601, end_iso8601
    
    else:
        return None, None


# Test the function
if __name__ == "__main__":
    date = "2023-11-02"
    time = "4:00pm - 7:00pm CST"
    
    start, end = this(date, time)
    
    print(start)
    print(end)