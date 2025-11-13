import random

print("Number Guessing Challenge")
print("I have secretly selected a number from 1 to 100.")
print("Try to figure it out with your guesses!\n")

while True:   # Wrap entire game in a loop so user can replay
    secret_number = random.randrange(1, 101)
    guess_count = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            # 10 attempts warning
            if guess_count == 10:
                print("⚠️ You've made 10 attempts!")

            # Guess comparison
            if guess < secret_number:
                print("Hint: Your guess is smaller than the number\n")
            elif guess > secret_number:
                print("Hint: Your guess is greater than the number\n")
            else:
                print(f"Great job! You figured out the number {secret_number}.")
                print(f"Total attempts taken: {guess_count}")

                # 🔁 Play again?
                play_again = input("Play again? (y/n): ").lower()
                if play_again != 'y':
                    exit()   # End the program completely
                else:
                    print("\nStarting a new game!\n")
                    break     # Restart outer loop

        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue
