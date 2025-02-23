def main_a():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))  # Convert input to integer
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers) / len(numbers):.2f}")


def main_b():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    input_username = input("Username: ")
    if input_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main_a()
main_b()
