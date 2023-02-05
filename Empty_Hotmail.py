import imapclient

# Replace the placeholders with your Hotmail email address and password
username = "your_email@hotmail.com"
password = "password_here"

# Connect to Hotmail's IMAP server
imap = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)
imap.login(username, password)

# Select the inbox and spam folders
imap.select_folder("inbox", readonly=False)
imap.select_folder("junk", readonly=False)

# Search for all messages and delete them
status, message_ids = imap.search(['ALL'])
message_ids = message_ids[0].split()

if message_ids:
    imap.delete_messages(message_ids)

# Expunge the deleted messages
imap.expunge()

# Log out
imap.logout()

# note that this will permanently delete all the emails
# in the inbox and spam folders, so be careful when running this script.

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/Empty_Hotmail.py
"""
