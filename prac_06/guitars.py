from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Names:")
while name:
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{guitars[-1]} added.\n")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
print("\n... snip ...\n")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

