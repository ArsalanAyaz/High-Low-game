import random

print("\n" * 2)

print("Welcome to the High-Low Guess Game")
print("This game has five rounds")

print()

ROUNDS = 5 
Score = 0

def play_game(round_number):
    global Score  

    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Round {round_number}")
    print(f"Your number = {your_number}")
    
    guess = input("What do you think, is your number 'higher' or 'lower' than the computer's number? (or type 'exit' to quit): ").lower()

    while guess not in ["higher", "lower", "exit"]:
        guess = input("Please enter 'higher', 'lower', or 'exit': ").lower()

    if guess == "exit":
        return False  # Return False to signal that the user wants to exit

    if (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
        print(f"You're right! The computer's number was = {computer_number}")
        Score += 1  
    else:
        print(f"You're incorrect! The computer's number was = {computer_number}")
        
    print()
    return True  # Continue the game

# Main game loop
for i in range(1, ROUNDS + 1):
    if not play_game(i):  # If play_game returns False, break the loop
        print()
        print("You chose to exit the game early.")
        break

print(f"Thanks for playing the game! Your final score is: {Score}")
