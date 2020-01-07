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
    
# Create the roll ASCII image
def d_img(rolls):
    roller = {
        1: ["|       |","|   o   |","|       |"],
        2: ["|    o  |","|       |","|  o    |"],
        3: ["|    o  |","|   o   |","|  o    |"],
        4: ["| o   o |","|       |","| o   o |"],
        5: ["| o   o |","|   o   |","| o   o |"],
        6: ["| o   o |","| o   o |","| o   o |"]
    }
    d_img_str = "\n"
    for dice in range(len(rolls)):
        d_img_str += "---------" + "   "
    d_img_str += "\n"
    for line in range(3):
        for roll in rolls:
            d = roller.get(roll, ["|       |","\n|       |","\n|       |"])
            d_img_str += d[line] + "   "
        d_img_str += "\n"
    for dice in range(len(rolls)):
        d_img_str += "---------" + "   "
    d_img_str += "\n"
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
total = 0
for roll in range(1, d_int+1):
    result = randint(1, s_int)
    rolls.append(result)
    total += result
    print("Roll #" + str(roll) + ": " + str(result))

print("\nTOTAL: " + str(total))
    
# If rolling d6, then add ASCII image as well
if s_int == 6:
    print(d_img(rolls))