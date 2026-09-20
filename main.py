import random as rand

choice = [1, -1, 0]

while True:

    try:

        computer = rand.choice(choice)

        youStr = input("Enter your choice : ")

        if youStr == "e":
            print("Programm was exited by user")
            break

        youDict = {"s" : 1, "w" : -1, "g" : 0}
        you = youDict[youStr]

        if (you == 1 and computer == -1):
            print("You Win!\n")

        elif (you == 1 and computer == 0):
            print("You Lose!\n")

        elif (you == -1 and computer == 0):
            print("You Win!\n")

        elif (you == -1 and computer == 1):
            print("You Lose!\n")

        elif (you == 0 and computer == 1):
            print("You Win!\n")

        elif (you == 0 and computer == -1):
            print("You Lose!\n")

        elif you == computer:
            print("That was a Tie!\n")

        else:
            print("That was Invalid input")

    except ValueError:
        print("Please enter a valid value\n")

    except KeyError:
        print("Please enter a valid value\n")

    except KeyboardInterrupt:
        print("Keyboard Interrupted do you want to exit enter 'e'")

    except EOFError:
        print("Please enter a valid value\n")