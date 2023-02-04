import os
from google.oauth2.credentials import Credentials
import google.auth
from googleapiclient.discovery import build
from googleapiclient import errors

# Authenticate the user
creds = Credentials.from_authorized_user_file(os.path.expanduser("~/.credentials/gmail-python-quickstart.json"))

try:
    # Connect to the Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Get the Spam label
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    spam_label = None
    for label in labels:
        if label['name'] == 'SPAM':
            spam_label = label
            break
    
    # Delete the Spam label and all the messages in it
    if spam_label:
        service.users().labels().delete(userId='me', id=spam_label['id']).execute()
        print('Spam label deleted.')
    else:
        print('Spam label not found.')

except HttpError as error:
    print(f'An error occurred: {error}')
