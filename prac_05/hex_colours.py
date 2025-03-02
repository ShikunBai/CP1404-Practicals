NAME_TO_COLOR = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Alice Blue": "#f0bf1a",
    "Alizarin Crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "Antique White": "#faebd7",
    "Antique White1": "#ffefdb",
    "Antique White2": "#eedfcc"
}

color_name = input("Enter color name: ").strip().title()
while color_name != "":
    try:
        print(f"{color_name} is {NAME_TO_COLOR[color_name]}")
    except KeyError:
        print("Invalid color name.")
    color_name = input("Enter color name: ").strip().title()

print("Thank you")