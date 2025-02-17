"""Q1"""
def question_1():
    name = input("Enter your name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()
"""Q2"""
def question_2():
    in_file = open("name.txt", "r")
    name = in_file.read()
    print(f"Hi, {name}!")
    in_file.close()
"""Q3"""
def question_3():
    with open("numbers.txt", "r") as in_file:
       first_number = int(in_file.readline())
       second_number = int(in_file.readline())
    total = first_number + second_number
    print(total)
"""Q4"""
def question_4():
    with open("numbers.txt", "r") as in_file:
       total = 0
       for line in in_file:
           total += int(line)
    print(total)


question_1()
question_2()
question_3()
question_4()