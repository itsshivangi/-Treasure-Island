print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Go left or right? ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. Swim or wait? ").lower()
    if choice2 == "wait":
        choice3 = input("You see three doors: red, yellow, and blue. Choose one: ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("Burned by fire. Game over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")
