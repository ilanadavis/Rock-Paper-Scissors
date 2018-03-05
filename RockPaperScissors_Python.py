import random

print("Welcome to Rock, Paper, Scissors!")
player1 = raw_input("Please enter one of the following: Rock, Paper, Scissors: ").lower()


gameList = ['rock','paper','scissors']

computer = random.choice(gameList)

print("Computer entered: " + computer)
print("Player1 entered: " + player1)
      


if player1 == computer:
    print("It's a draw!")
elif player1 == "rock" and computer=="scissors":
    print("Player1 you win!")
elif player1 == "paper" and computer=="rock":
    print("Player1 you win!")
elif player1 == "scissors" and computer=="paper":
    print("Player1 you win!")

elif computer == "rock" and player1=="scissors":
    print("Computer wins!")
elif computer == "paper" and player1=="rock":
    print("Computer wins!")
elif computer == "scissors" and player1=="paper":
    print("Computer wins!")
    
