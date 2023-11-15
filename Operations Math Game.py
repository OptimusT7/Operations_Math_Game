import random
import math
import time

TGREEN = "\033[32m"
TYELLOW = "\033[33m"
TORANGE = "\033[31;33m"
TBOLD = "\033[1m"
TNOEFFECT = "\033[0m"
play_again = "y"

temp = 0

while play_again == "y":
    print("\n\n")
    max_number = input("What is the starting maximum number you wish the randomiser to be able to choose (3 - 100): ").strip()

    while not max_number.isdigit() or int(max_number) not in range(3, 101):
        print("Please enter a whole number, min = 3, max = 100")
        max_number = input(
            "\nWhat is the maximum number you wish the randomiser to be able to choose (3 - 100): "
        )

    streak = 0
    lives = 3
    max_number = int(max_number)
    num1 = 0
    num2 = 0

    def correct():
        print(TGREEN + "\n\nCorrect! You guessed the number!\n\n" + TNOEFFECT)
        print(f"You have a current streak of {str(streak)}")

    print("You have 3 lives - every time you guess incorrectly you lose a life")
    time.sleep(2)
    while lives > 0:
        num1 = random.randint(1, max_number)
        num2 = random.randint(1, max_number)

        addition = num1 + num2
        subtraction1 = num1 - num2
        subtraction2 = num2 - num1
        multiplication = num1 * num2
        division1 = num1 / num2
        division2 = num2 / num1
        power1 = num1**num2
        power2 = num2**num1
        root1 = num1 * math.sqrt(num2)
        root2 = num2 * math.sqrt(num1)
        operations = [
            addition,
            subtraction1,
            subtraction2,
            multiplication,
            division1,
            division2,
            power1,
            power2,
            root1,
            root2,
        ]

        print(f"The max number for this round is {max_number}")
        print(
            "\n\nThe following numbers are all either:\n" + TBOLD +
            "N1 + N2, N1 - N2, N2 - N1, N1 * N2, N1/N2, N2/N1, N1^N2, N2^N1, N1 * √N2, N2 * √N1"
            + TNOEFFECT
        )

        print(
            "\nTry to figure out the second number using the following (rounded to 6 decimal places when necessary):\n"
        )

        loop = len(operations)
        for x in range(0, 3):
            successful = False
            while not successful:
                a = random.choice(operations)
                operations.remove(a)
                try:
                    if len(str(a)) < 100:
                        print(str(f"{round(a, 6):,}"))
                        successful = True
                except:
                    pass

        print(TBOLD + f"\nThe first number is {num1}\n" + TNOEFFECT)

        # guess
        g = input(f"What is the second number (you have {lives} lives remaining): ")

        while not g.isdigit() or int(g) == 0:
            print("Please enter a whole positive number\n")
            g = input("What is the second number: ")
        if int(g) == num2:
            streak += 1
            max_number += math.floor((max_number + 10) / 10)
            correct()
        else:
            a = 1
            lives -= 1

            while a == 1 and lives > 0:
                if lives == 1:
                    print(TYELLOW + f"Incorrect! You have 1 life left" + TNOEFFECT)
                else:
                    print(
                        TYELLOW + f"Incorrect! You have {lives} lives left" + TNOEFFECT
                    )

                g = input("\nWhat is the second number: ")

                while not g.isdigit():
                    print("Please enter a number\n")
                    g = input("What is the second number: ")

                if int(g) == num2:
                    streak += 1
                    a = 0
                    max_number += math.floor((max_number + 10) / 10)
                    correct()
                else:
                    lives -= 1

    print(
        TYELLOW
        + "You ran out of lives!"
        + f"\nNumber 2 was equal to {num2}"
        + TNOEFFECT
        + TBOLD
        + f"\n\nYou died with a streak of {streak}. Well done!"
        + TNOEFFECT
    )

    play_again_ask = input("\nDo you wish to play again? (Y/N): ").lower().strip()
    while play_again_ask not in ("y", "n"):
        play_again_ask = input(
            "Please enter either 'y' or 'n'\n\nDo you wish to play again? (Y/N): "
        )

input("Press enter to close")
