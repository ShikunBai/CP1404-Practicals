"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print(data)
    for pair in data:
        subject = pair[0]
        lecturer = pair[1]
        student_numbers = pair[2]
        print("{} is taught by {} and has {} students.".format(subject, lecturer, student_numbers))


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    pairs = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the newline character
            parts = line.split(',')  # Split the line into parts
            parts[2] = int(parts[2])  # Convert student count to integer
            pairs.append(parts)
    return pairs


main()
