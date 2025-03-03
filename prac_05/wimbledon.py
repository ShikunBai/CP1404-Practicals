import csv

FILENAME = "wimbledon.csv"

def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def load_records(filename):
    """Load data from a CSV file using csv.reader()."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            records.append(row)
    return records

def process_records(records):
    """Process data to count champions and their countries."""
    champion_to_count = {}
    countries = set()

    for record in records:
        countries.add(record[1])
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1

    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display the results."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

    main()
