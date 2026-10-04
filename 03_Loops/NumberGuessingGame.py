"""Random number guessing game between a computer and human, where the computer picks a  
random number, the human tries to guess it, and the computer hints if the guess is too low or high,
then ends the loop if the guess is correct"""

import random

Lower_boundary = 1
Upper_boundary = 100
maxAttempts = 10

def hint(guess: int, secret: int) -> str:
    #Compare guess to randomly selected number and return a hint
    if guess < secret:
        return "Lower than expected"
    elif guess > secret:
        return "Way too High!!!"
    return "Correct!"

def playGame()-> None:
    secret = random.randint(Lower_boundary, Upper_boundary)
    guesses = []

    print(f"\nI'm thinking of a number between {Lower_boundary} and {Upper_boundary}")


    while len(guesses)< maxAttempts:
        hmnGuess = input(f"\nYour Guess {len(guesses) + 1}/{maxAttempts}: ").strip()
        if not hmnGuess.isdigit():
            print("Please, enter a whole number.")
            continue

        guess = int(hmnGuess)
        if not Lower_boundary <= guess <= Upper_boundary:
            print(f"Pick a number between {Lower_boundary} and {Upper_boundary}.")
            continue
    
        guesses.append(guess)
        print(hint(guess, secret))

        if guess == secret:
            print("You're absolutely positively correct. You got it in {len(guesses)} attempts")
            break
    else:
        print("You've maxed out on number of attempts. The number was {secret}.")

    print("\nYour guesses: ")
    for number, g in enumerate(guesses, start=1):
                print(f"  {number}. {g}")
    
    return len(guesses) if secret in guesses else None


def main() -> None:
    bestScore = None
    while True:
        result = playGame()

        if result is not None:
            if bestScore is None or result < bestScore:
                bestScore = result
                print("New best score!")
        if bestScore is not None:
            print(f"Best score so far: {bestScore}")
        replay= input("Play again? (y/n): ").strip().lower()
        if replay != "y":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()