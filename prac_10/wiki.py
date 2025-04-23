"""
CP1404 Practical
Wikipedia API Program
"""

import wikipedia


def main():
    """Prompt user for a Wikipedia page title and display its info, with error handling."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(title, sentences=2))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5], "...")
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        title = input("Enter page title: ").strip()
    print("Thank you")

if __name__ == '__main__':
    main()
