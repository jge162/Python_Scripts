import imapclient
import json
import os
# Replace the placeholders with your Hotmail email address and password
with open(os.path.expanduser("~/.credentials/gmail-python-quickstart.json"), 'rb') as f:
  data = json.load(f)
  
# Connect to Hotmail's IMAP server
imap = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)
imap.login(data['username'], data['password'])

# Select the inbox and spam folders
imap.select_folder("inbox", readonly=False)
imap.select_folder("spam", readonly=False)

# Search for all messages and delete them
_, message_ids = imap.search(['ALL'])
imap.delete_messages(message_ids)

# Expunge the deleted messages
imap.expunge()

# Log out
imap.logout()

# note that this will permanently delete all the emails 
# in the inbox and spam folders, so be careful when running this script.
