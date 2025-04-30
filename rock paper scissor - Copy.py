import random

# Options
choices = ['rock', 'paper', 'scissors']

# Player choice
player = input("Enter rock, paper, or scissors: ").lower()

# Computer choice
computer = random.choice(choices)

print(f"Computer chose: {computer}")

# Check who wins
if player == computer:
    print("It's a tie!")
elif (player == 'rock' and computer == 'scissors') or \
     (player == 'paper' and computer == 'rock') or \
     (player == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("You lose!")