import random

rounds = 1
drawScore = 0
winScore = 0
lostScore = 0

print("Welcome to Rock Paper Scissor v/s Computer")
print("There will be 5 round in total\n")

while rounds <= 5:

    print(f"Round {rounds} begins...")
    lst = ["Rock", "Paper", "Scissor"]
    computerChoice = random.choice(lst)

    userChoice = input("Choose Rock, Paper, or Scissor\n")
    userChoice = userChoice.capitalize()

    if computerChoice == "Rock":
        if userChoice == "Rock":
            print(f"Computer Choose {computerChoice}")
            print("Draw")
            drawScore += 1

        elif userChoice == "Paper":
            print(f"Computer Choose {computerChoice}")
            print("You Win")
            winScore += 1

        elif userChoice == "Scissor":
            print(f"Computer Choose {computerChoice}")
            print("You Loose")
            lostScore += 1

        else:
            print("Wrong Input")

    elif computerChoice == "Paper":
        if userChoice == "Paper":
            print(f"Computer Choose {computerChoice}")
            print("Draw")
            drawScore += 1

        elif userChoice == "Scissor":
            print(f"Computer Choose {computerChoice}")
            print("You Win")
            winScore += 1

        elif userChoice == "Rock":
            print(f"Computer Choose {computerChoice}")
            print("You Loose")
            lostScore += 1

        else:
            print("Wrong Input")

    else:
        if userChoice == "Scissor":
            print(f"Computer Choose {computerChoice}")
            print("Draw")
            drawScore += 1

        elif userChoice == "Rock":
            print(f"Computer Choose {computerChoice}")
            print("You Win")
            winScore += 1

        elif userChoice == "Paper":
            print(f"Computer Choose {computerChoice}")
            print("You Loose")
            lostScore += 1

        else:
            print("Wrong Input")

    rounds += 1
    print("\n\n")

print("SCORE BOARD")
print(f"\n\nPLAYER WIN - {winScore} OUT OF 5")
print(f"COMPUTER WIN - {lostScore} OUT OF 5")
print(f"MATCH DRAW -  {drawScore} OUT OF 5")
