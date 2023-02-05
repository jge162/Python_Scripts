import imaplib
import os
import json

with open(os.path.expanduser("~/.credentials/icloud-python-quickstart.json"), 'r') as f:
  data = json.load(f)
# Replace the placeholders with your iCloud email address and password

# Connect to iCloud's IMAP server
imap = imaplib.IMAP4_SSL("imap.mail.me.com")
imap.login(data['username'], data['password'])

# Select the spam folder
imap.select("Spam", readonly=False)

# Search for all messages and delete them
_, message_ids = imap.search(None, "ALL")
message_ids = message_ids[0].split()
for message_id in message_ids:
    imap.store(message_id, "+FLAGS", "\\Deleted")

# Expunge the deleted messages
imap.expunge()

# Log out
imap.close()
imap.logout()

# this will permanently delete all the emails 
# in the spam folder, so be careful when running this script.
