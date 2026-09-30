import random
computer_choice = random.randint(1,10)
while True:
    your_choice = int(input("Enter your choice :"))

    if your_choice==computer_choice:
        print("correct choice")
        break

    elif your_choice>computer_choice:
        print("less than")

    elif your_choice<computer_choice:
        print("greater than")

    else:
        print("invailid choice")
