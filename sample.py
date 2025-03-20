from garminconnect import Garmin
import json
import getpass  # Secure password input

# Prompt user for credentials
email = input("Enter your Garmin email: ")
password = getpass.getpass("Enter your Garmin password: ")  # Secure input

try:
    # Authenticate with Garmin Connect
    client = Garmin(email, password)
    client.login()

    # Fetch today's step count
    steps_data = client.get_steps_data("today")

    # Fetch heart rate data
    heart_rate_data = client.get_heart_rates("today")

    # Fetch body composition data (if available)
    body_composition = client.get_body_composition("today")

    # Print the results
    print("\nSteps Data:", json.dumps(steps_data, indent=4))
    print("\nHeart Rate Data:", json.dumps(heart_rate_data, indent=4))
    print("\nBody Composition:", json.dumps(body_composition, indent=4))

except Exception as e:
    print(f"Error: {e}")
