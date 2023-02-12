import string
import random


def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = "".join(random.choice(characters) for i in range(length))

    return password


# Example usage
password_length = 16
password = generate_password(password_length)
print("Password:", password)

"""
Generate a random password of a given length
"""
