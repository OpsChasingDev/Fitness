from garminconnect import Garmin
import json

# Replace with your Garmin credentials
EMAIL = "your-email@example.com"
PASSWORD = "your-password"

try:
    # Authenticate with Garmin Connect
    client = Garmin(EMAIL, PASSWORD)
    client.login()

    # Fetch today's step count
    steps_data = client.get_steps_data("today")

    # Fetch heart rate data
    heart_rate_data = client.get_heart_rates("today")

    # Fetch body composition data (if available)
    body_composition = client.get_body_composition("today")

    # Print the results
    print("Steps Data:", json.dumps(steps_data, indent=4))
    print("Heart Rate Data:", json.dumps(heart_rate_data, indent=4))
    print("Body Composition:", json.dumps(body_composition, indent=4))

except Exception as e:
    print(f"Error: {e}")
