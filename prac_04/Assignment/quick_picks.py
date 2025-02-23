import random
NUMBERS_PER_PICK = 6
LOWEST_NUMBER = 1
LARGEST_NUMBER = 45


pick_amount = int(input("How many quick picks? "))
for i in range(pick_amount):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(LOWEST_NUMBER, LARGEST_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))