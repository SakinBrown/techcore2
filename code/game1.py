import random

def guessing_numbers():
    print('Welcome to GN! Guessing Num!\n')
    print('Level 1!')

    # Generate the random number
    dupe = random.randint(1, 10)

    def guess_loop():
        try:
            guess = int(input('Guess the number between 1 and 10!: '))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                guess_loop()  # Recursive call for invalid input
            elif guess == dupe:
                print('You win!')
            elif guess > dupe:
                print('Too Big. Try again.')
                guess_loop()  # Recursive call for incorrect guess
            else:
                print('Too Small. Try again.')
                guess_loop()  # Recursive call for incorrect guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            guess_loop()  # Recursive call for invalid input

    # Start the guessing loop
    guess_loop()

if __name__ == "__main__":
    guessing_numbers()

def guessing_numbers2():
    print('Welcome to GN! Guessing Num!\n')
    print('Level 1!')

    # Generate the random number
    dupe2 = random.randint(1, 10)

    def guess_loop2():
        try:
            guess2 = int(input('Guess the number between 1 and 50!: '))

            if guess2 < 1 or guess2 > 50:
                print("Please enter a number between 1 and 50.")
                guess_loop2()  # Recursive call for invalid input
            elif guess2 == dupe2:
                print('You win!')
            elif guess2 > dupe2:
                print('Too Big. Try again.')
                guess_loop2()  # Recursive call for incorrect guess
            else:
                print('Too Small. Try again.')
                guess_loop2()  # Recursive call for incorrect guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            guess_loop2()  # Recursive call for invalid input

    # Start the guessing loop
    guess_loop2()

if __name__ == "__main__":
    guessing_numbers2()
