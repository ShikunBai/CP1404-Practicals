import csv
from prac_07.guitar import Guitar

def main():
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
    for guitar in guitars:
        print(guitar)
main()