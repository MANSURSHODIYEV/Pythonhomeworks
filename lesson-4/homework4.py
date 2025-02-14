import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("You guessed it right! Congratulations!")
            return
        
        attempts -= 1
        print(f"Attempts left: {attempts}")
    
    print("You lost. Want to play again?")
    retry = input("Type 'Y', 'YES', 'y', 'yes', 'ok' to play again: ")
    if retry.lower() in ['y', 'yes', 'ok']:
        play_game()
    else:
        print("Thanks for playing!")

play_game()