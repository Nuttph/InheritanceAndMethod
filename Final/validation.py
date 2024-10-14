import re

def is_valid_email(email):
    # Define the regex pattern for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
test_emails = [
    "example@example.com",
    "user.name+tag+sorting@example.com",
    "user@sub.example.com",
    "invalid-email.com",
    "another.invalid@.com"
]

for email in test_emails:
    print(f"{email}: {is_valid_email(email)}")
