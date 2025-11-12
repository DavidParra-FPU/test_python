import random as rand
print("Welcome to Rock-Paper-Scissors!")
computer = ""
choiceC = rand.randrange(0,2)
choice = input("rock, paper, or scissors: ")
print(f"You chose: {choice}")
if choiceC ==1:
  computer = "Rock"
elif choiceC==2:
  computer == "Scissors"
else:
  computer == "Paper"
print(f"Computer chose: {computer}")

