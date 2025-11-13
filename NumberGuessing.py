import random

print("Number Guessing Challenge")
print("I have secretly selected a number from 1 to 100.")
print("Try to figure it out with your guesses!\n")

# Ek random number choose karna (1–100 range)
secret_number = random.randrange(1, 101)

# Guess count track karne ke liye
guess_count = 0

while True:
    try:
        user_input = input("Your guess: ")
        guess = int(user_input)
        guess_count += 1

        # Guess ki comparison
        if guess < secret_number:
            print("Hint: Your guess is smaller than the number\n")
        elif guess > secret_number:
            print("Hint: Your guess is greater than the number\n")
        else:
            print(f"Great job! You figured out the number {secret_number}.")
            print(f"Total attempts taken: {guess_count}")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a whole number.\n")
