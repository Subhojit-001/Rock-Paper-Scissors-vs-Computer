import random

a = 1
d = 0
w = 0
l = 0

while a <= 5:

    lst = ["Rock", "Paper", "Scissor"]
    c = random.choice(lst)

    n = input("Choose Rock, Paper, or Scissor\n")
    n = n.capitalize()

    if c == "Rock":
        if n == "Rock":
            print(f"Computer Choose {c}")
            print("Draw")
            d += 1

        elif n == "Paper":
            print(f"Computer Choose {c}")
            print("You Win")
            w += 1

        elif n == "Scissor":
            print(f"Computer Choose {c}")
            print("You Loose")
            l += 1

        else:
            print("Wrong Input")

    elif c == "Paper":
        if n == "Paper":
            print(f"Computer Choose {c}")
            print("Draw")
            d+=1

        elif n == "Scissor":
            print(f"Computer Choose {c}")
            print("You Win")
            w+=1

        elif n == "Rock":
            print(f"Computer Choose {c}")
            print("You Loose")
            l+=1

        else:
            print("Wrong Input")

    else:
        if n == "Scissor":
            print(f"Computer Choose {c}")
            print("Draw")
            d+=1

        elif n == "Rock":
            print(f"Computer Choose {c}")
            print("You Win")
            w+=1

        elif n == "Paper":
            print(f"Computer Choose {c}")
            print("You Loose")
            l+=1

        else:
            print("Wrong Input")

    a+=1


print(f"\n\nYou win {w} times")
print(f"You loose {l} time")
print(f"You draw {d} time")