
import imaplib

# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Login to your Gmail account
mail.login( 'YOUR_EMAIL@gmail.com', 'YOUR_GMAIL_PASSWORD')

# List the email folders in your account
typ, data = mail.list()
for folder in data:
    print(folder.decode())

# Select the spam folder
typ, data = mail.select('"[Gmail]/Spam"')

# Search for all messages in the spam folder
typ, data = mail.search(None, 'ALL')

# Delete all messages in the spam folder
if data:
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.expunge()

# Close the mailbox and log out
mail.close()
mail.logout()

print('All messages from the spam folder have been Deleted Successfully.')
