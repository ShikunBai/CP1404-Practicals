"""
Emails
Estimate: 20 minutes
Actual:   50 minutes
"""


def main():
    """Main function to get email-name pairs in a dictionary."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        guessed_name = get_name_from_email(email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").strip().title()
        else:
            name = guessed_name
        email_to_name[email] = name
        email = input("Email: ").strip()

def get_name_from_email(email):
    """Get name from the email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name