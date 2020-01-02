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
print("\nRolling... ")
for roll in range(1, d_int+1):
	result = randint(1, s_int)
	print("Roll #" + str(roll) + ": " + str(result))