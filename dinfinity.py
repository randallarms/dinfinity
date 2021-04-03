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
    try:
        return True, int(n)
    except ValueError:
        return False, 0
    

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


# Exit phrase array & check var
exiters = ["exit", "quit", "leave", "n", "no", "negative"]
r_in = "y"

# Run the prompt and print the results
while r_in not in exiters:
    rolls = []
    
    # Input number of sides on each die
    print("\nHow many sides on each die? ")
    s_in = input("> ");

    # Check if int and convert
    s_check, s_int = int_check(s_in)

    # Input number of dice to roll
    print("\nHow many dice to roll? ")
    d_in = input("> ");

    # Check if int and convert
    d_check, d_int = int_check(d_in)
    
    # Check the input
    if d_check is False or s_check is False:
        print("\nInput numbers must be integers. ")
    elif d_int < 1 or s_int < 1:
        print("\nInput numbers must be greater than 0. ")       
    else:
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
            
    print("\nWould you like to roll again? (y/n) ")
    r_in = input("> ")


#Salutations and exit
print("\nThank you for using dInfinity. Goodbye! \n")
exit()
        