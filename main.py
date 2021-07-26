import random
# game() will implement the logic for game.
def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("Computers Turn: Snake(s) Water(w) Gun(g) ? ")
randNo = random.randint(1,3)  # This function will print random number between 1 and 2.
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(s) Water(w) Gun(g) ? ")

a = game(comp, you)
print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You loose!")
