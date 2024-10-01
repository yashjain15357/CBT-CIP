import random
import time

def rps():
    global points
    options = ["ROCK", "PAPER", "SCISSOR"]
    print(f"{name}, type your option: \n1>> ROCK\n2>> PAPER\n3>> SCISSOR")
    user_input = input().lower()

    if user_input == "rock":
        e = 0
    elif user_input == "paper":
        e = 1
    elif user_input == "scissor":
        e = 2
    else:
        e = 3

    d = random.randint(0, 2)
    print(options[d])

    return d, e

# Main code
name = input("Enter your name: ")
points = 0
print(f"Now your game starts \n{name} VS computer")

while True:
    d, e = rps()
    if d == e:
        points += 0
    elif (d == 0 and e == 1) or (d == 2 and e == 0) or (d == 1 and e == 2):
        points += 1
    elif (d == 0 and e == 2) or (d == 2 and e == 1) or (d == 1 and e == 0):
        points -= 1
    elif e == 3:
        points += 0

    print(f"Your Total Points = {points}")
    if points==3:
        print(f"congrulation {name} you win")
        break
    if(points== -3):
        print(f"{name} you loose ")
        print("Better luck for next time")
        break

