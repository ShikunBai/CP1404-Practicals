MIN_LENGTH = 8


def main():
    """Main function to get and verify password and print asterisks."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a password that meets the minimum length."""
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password, symbol='*'):
    """Print a line of symbols equal to the length of the password."""
    print(symbol * len(password))


if __name__ == '__main__':
    main()