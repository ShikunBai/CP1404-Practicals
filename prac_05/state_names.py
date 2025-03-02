"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}
CODE_LENGTH = 3

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

try:
    print(f"{state_code} is {CODE_TO_NAME[state_code]}")
except KeyError:
    print("Invalid short state")
state_code = input("Enter short state: ").upper()

for code, name in CODE_TO_NAME.items():
    print(f"{code:<{CODE_LENGTH}} is {name}")
