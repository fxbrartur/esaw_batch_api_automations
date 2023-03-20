import json
import requests
import time

# Replace this with the URL of your endpoint
endpoint_url_template = "https://latam.esignanywhere.net/v5/user/{id}"

# Replace this with your API key or authentication token, if necessary
apitoken = "{apitoken}"

# Load the JSON string from the file
with open("users.json", "r") as file:
    json_string = file.read()

# Parse the JSON string into a Python object
data = json.loads(json_string)

# Get the list of users from the "Entries" key
users = data["Entries"]

# Iterate over the list of users
for user in users:
    # Extract the ID and email from the user object
    user_id = user["Id"]
    user_email = user["Email"]

    if not user_email:
        print(f"No email found for user {user_id}")
        continue

    # Create the URL for this user
    user_endpoint_url = endpoint_url_template.format(id=user_id)

    # Create the request body with the email placeholder replaced
    request_body = {
        "Authentications": [
            {
                "ProviderName": "Insert your provider name here",
                "UserIdentifierAttibuteValue": user_email,
                "DiscriminatorType": "UserAuthenticationSaml"
            }
        ]
    }

    # Make the PATCH request to the user endpoint
    response = requests.patch(user_endpoint_url, json=request_body, headers={"apitoken": apitoken})

    # Print the response status code and any error messages
    if not response.ok:
        print(f"User {user_id} - Status code: {response.status_code}")
    else:
        print(f"User {user_id} - Status code: {response.status_code}")

    # Wait for 2 seconds before making the next request
    time.sleep(2)
