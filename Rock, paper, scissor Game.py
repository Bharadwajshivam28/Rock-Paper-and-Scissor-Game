import random

#Rock Paper scissors Game
def game(comp, you):
    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #check for all possibilaties when computer chose r
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    #check for all possibilaties when computer chose p
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    #check for all possibilaties when computer chose s
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Comp turn: Rock(r) Paper(p) Scissors(s)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("Your turn: Rock(1) Paper(2) Scissor(3)?")
a = game(comp, you)

print(f"Computer chose{comp}")
print(f"you chose{you}")

if a == None:
    print("The game is a Tie!")
elif a:
    print("You win!")
else:
    print("You lose!")