import csv
import json
import requests
import time
from tqdm import tqdm

# API endpoint URL and API token for the latam v5 instance, fill free to change it.
url = 'https://latam.esignanywhere.net/api/v5.0/user/create'
headers = {'apitoken': {APITOKEN}}

# read CSV file
with open('users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # count number of rows (excluding header row)
    num_rows = sum(1 for row in reader) - 1

    # reset reader to start at the beginning of the file
    csvfile.seek(0)
    next(reader)  # skip header row

    # create new CSV file for response data
    with open('responses.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # write header row for response data
        writer.writerow(['Status Code', 'Content'])

        # create and send JSON object for each row
        for row in tqdm(reader, total=num_rows):
            # create dictionary with placeholders and values
            obj = {
                "UserDescription": {
                    "Email": row[2],
                    "FirstName": row[0],
                    "LastName": row[1],
                    "NotifyRecipientOnActionNeeded": row[3],
                    "NotifySenderCompleteEnvelope": row[3],
                    "NotifySenderDeclined": row[3],
                    "NotifySenderDeliveryFailed": row[3],
                    "NotifySenderViewed": row[3],
                    "Roles": [
                        "Power User"
                    ],
                    "Authentications": []
                },
                "UserActivationDescriptor": {
                    "SendInvitationMail": row[3],
                    "ForcePasswordReset": row[3]
                }
            }

            # make POST request with JSON data as body and ApiToken header
            response = requests.post(url, json=obj, headers=headers)

            # print response status code and content
            print(f'Response {response.status_code}\n{response.content}\n')

            # write response data to CSV file
            writer.writerow([response.status_code, response.content])

            # wait for 2 seconds before sending the next request
            time.sleep(2)
