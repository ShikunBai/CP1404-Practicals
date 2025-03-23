import csv
from prac_07.guitar import Guitar

def main():
    guitars = read_file()
    print("Do you want add your new guitars?")
    name = input("Name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("New guitar added.")
        name = input("Name: ")
    guitars.sort()
    write_file(guitars)
    for guitar in guitars:
        print(guitar)


def read_file():
    """Read csv file and generate list for guitars"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        # print(parts)
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    guitars.sort()
    in_file.close()
    return guitars

def write_file(guitars):
    """Write new guitars to csv file"""
    guitars_file = open('guitars.csv', 'w')
    writer = csv.writer(guitars_file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year])

if __name__ == "__main__":
    main()