# Formatting datetime object into a more readable string using strftime()
# %Y: Year with century (e.g., 2025)
# %m: Month as a zero-padded decimal number (e.g., 05)
# %d: Day of the month as a zero-padded decimal number (e.g., 13)
# %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 15)
# %I: Hour (12-hour clock) as a zero-padded decimal number (e.g., 03)
# %M: Minute as a zero-padded decimal number (e.g., 36)
# %S: Second as a zero-padded decimal number (e.g., 30)
# %p: Locale’s equivalent of either AM or PM.
# %A: Locale’s full weekday name (e.g., Tuesday)
# %B: Locale’s full month name (e.g., May)

import requests # pip install requests
import json
from datetime import datetime

_timezone = "America/Los_Angeles"
_url_endpoint = "http://worldtimeapi.org/api/timezone/America/Los_Angeles"
print(f"*** Making an API request to: {_url_endpoint} ***\n")

try:
    # Send a GET request to the URL, with a timeout of 5 seconds
    response = requests.get(_url_endpoint, timeout=5)

    # Check if the request returned an HTTP error
    response.raise_for_status()

    # If no error, print success message
    print(f"\nRequest to API successful! Status code: {response.status_code}\n")

    # Parse the JSON respone into a dictionary
    wt_data = response.json()

    # Print the dictionary
    print("\nRaw Python dictionary from JSON:")
    print(json.dumps(wt_data, indent=2))

    # Extract datetime key
    date_time_str = wt_data.get("datetime")
    print(f"\nExtracted datetime string: {date_time_str}\n")

    # Convert into a readable format
    dt_object = datetime.fromisoformat(date_time_str)

    # Convert ISO string into readable format
    formatted_time = dt_object.strftime("%I:%M:%S")
    formatted_date = dt_object.strftime("%A, %B %d, %Y")

    # Print the current time to the user
    print(f"The current time in {_timezone} is: {formatted_date} - {formatted_time} {wt_data.get('abbreviation')}\n")

except requests.exceptions.HTTPError as e_http:
    print(f"\nAn HTTP error occured: {e_http}\n")
except requests.exceptions.ConnectionError as e_conn:
    print(f"\nA connection error occured: {e_conn}\n")
except requests.exceptions.Timeout as e_timeout:
    print(f"\nThe request timed out: {e_timeout}\n")
except requests.exceptions.RequestException as e_general:
    print(f"\nAn error occured with the request: {e_general}\n")
except json.JSONDecodeError:
    print("\nFailed to decode JSON from the response\n")