"""
Programming Language
Estimate time: 30 minutes
Actual time: 20 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

def main():
    languages = [
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

    for language in languages:
        print(language)
    print(f"The dynamically typed language are:")
    for language in languages:
        if language.is_dynamic() == True:
            print(language.name)

main()