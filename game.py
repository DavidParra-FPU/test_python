import random as rand
print("Welcome to Rock-Paper-Scissors!")
computer = ""
choice = rand.randrange(0,2)
if choice ==1:
  computer = "Rock"
elif choice ==2:
  computer == "Scissors"
else:
  computer == "Paper"
print(f"Computer chose: {computer}")
