#=====================================#
#             dInfinity               #
#          by Randall Arms            #
# @ github.com/randallarms/dinfinity  #
#=====================================#

from random import randint

# Opening text
print("\n\n\n=========")
print("dInfinity")
print("=========")
print("Roll the dice!")

# Rolls array
rolls = []

# Checks that the input n is a positive integer and returns an obj of int type
def int_check(n):
    if (int(n) < 1):
        print("\nInput number must be greater than 0. ")
        exit()
    try:
        return int(n)
    except ValueError:
        print("\nInput number must be an integer. ")
        exit()
        
# Create the 2d6 roll ASCII image
def d_img(r1, r2):
    roller = {
        1: ["|       |","|   o   |","|       |"],
        2: ["|    o  |","|       |","|  o    |"],
        3: ["|    o  |","|   o   |","|  o    |"],
        4: ["| o   o |","|       |","| o   o |"],
        5: ["| o   o |","|   o   |","| o   o |"],
        6: ["| o   o |","| o   o |","| o   o |"]
    }
    d1 = roller.get(r1, ["|       |","\n|       |","\n|       |"])
    d2 = roller.get(r2, ["|       |","\n|       |","\n|       |"])
    d_img_str = "\n---------   ---------\n"
    for line in range(3):
        d_img_str += d1[line] + "   " + d2[line] + "\n"
    d_img_str += "---------   ---------\n"
    return d_img_str

# Input number of sides on each die
print("\nHow many sides on each die? ")
s = input("> ");

s_int = int_check(s)

# Input number of dice to roll
print("\nHow many dice to roll? ")
d = input("> ");

d_int = int_check(d)

# Check for large numbers and confirm
if s_int > 100 or d_int > 100:
    print("\nThis roll is complex and may take a long time to finish. Type yes to confirm: ")
    confirm = input("> ");
    if confirm != "yes":
        print("\nRoll canceled. ")
        exit()

# Iterate through the integers and print results
print("\nRolling... \n")
for roll in range(1, d_int+1):
    result = randint(1, s_int)
    rolls.append(result)
    print("Roll #" + str(roll) + ": " + str(result))
    
# If rolling 2d6, then add ASCII image as well
if d_int == 2 and s_int == 6:
    print(d_img(rolls[0], rolls[1]))