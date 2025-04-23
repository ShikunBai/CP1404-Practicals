MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Main function to run the score menu program."""
    print("Welcome to the Score Menu Program!")
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Score result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter score (0–100): "))
    return score


def get_score_result(score):
    """Return a string representing the score result."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print as many stars as the score (rounded to nearest int)."""
    print("*" * int(round(score)))


if __name__ == '__main__':
    main()
