import random
import sys
import os

for i in [2,4,6,8,10]:
    print(i)

for i in range(2,10):
    print("i = ", i)

for i in range(1,10):
    print("i = ", i)

#i % 2 == 0 ---> even number
i = 2
print((i%2) == 0)


#Print out odd numbers from 1 - 20
for i in range(1,21):
    if((i % 2) != 0):
        print(i)


# working with floats

#your_float = input("Enter a float: ")

#your_float = float(your_float)

#print("Round to 2 decimals : {:.2f}".format(your_float))

#second problem

#money = input("How much to invest : ")
#interest_rate = input("Interest Rate : ")

#money = float(money)

#interest_rate = float(interest_rate) * .01

#for i in range(10):
 #   money = money + (money * interest_rate)

#print("Investment after 10 years : {:.2f}".format(money))



#random numbers

rand_num = random.randrange(1,51)

i = 1

while(i != rand_num):
    i += 1

print ("The random value is : ", rand_num)


i = 1

while i <= 20:
    if(i % 2) == 0:
        i += 1
        continue

    if( i == 15):
        break

    print("Odd : ", i)

    i += 1

# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# You should use a while loop and 3 for loops

# I know that this is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

# So I need to
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("How tall is the tree")
# Convert into an integer
tree_height = int(tree_height)
# Get the starting spaces for the top of the tree
spaces = tree_height - 1
# There is one hash to start that will be incremented
hashes = 1
# Save stump spaces til later
stump_spaces = tree_height - 1
# Makes sure the right number of rows are printed
while tree_height != 0:
    # Print the spaces
    # end="" means a newline won't be added
    for i in range(spaces):
        print(" ", end ="")
    # Print the hashes
    for i in range(hashes):
        print("#", end="")
    # Newline after each row is printed
    print()
    # I know from research that spaces is decremented by 1 each time
    spaces -= 1
    # I know from research that hashes is incremented by 2 each time
    hashes += 2
    # Decrement tree height each time to jump out of loop
    tree_height -= 1
# Print the spaces before the stump and then a hash
# Print the spaces before the stump and then a hash
for i in range(stump_spaces):
    print(" ", end="")

print("#")