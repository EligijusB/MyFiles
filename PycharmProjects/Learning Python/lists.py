import random
import math

#python lists can grow in size, can contain different types of data

randList = ["String", 1.234, 28]

oneToTen = list(range(10))

randList = randList + oneToTen

print(randList[0])

print("List Length :", len(randList))

first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("index of string: ", first3.index("String"))

print("how many strings: ", first3.count("String"))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))


#########PROBLEM 1##################

def randomListGenerator():
    randList = []

    for i in range(5):
        number = random.randrange(1,10)
        randList.append(number)

    print(randList)

randomListGenerator()

#####################################

#######BUBBLE SORT###########
# ---------- SORT A LIST : BUBBLE SORT ----------
# The Bubble sort is a way to sort a list
# It works this way
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

rand_List = []

for i in range(5):
    number = random.randrange(1, 10)
    rand_List.append(number)

length_of_list = len(rand_List) - 1

while length_of_list > 1:
    j = 0

    while j < length_of_list:
        if rand_List[j] > rand_List[j + 1]:
            temp = rand_List[j]
            rand_List[j] = rand_List[j + 1]
            rand_List[j + 1] = temp
        else:
            print()

        j += 1
    length_of_list -= 1

for k in rand_List:
    print(k, end=", ")
print()

######################################

#############PROBLEM 2##############

randList2 = []

for i in range(5):
    number = random.randrange(1, 10)
    randList2.append(number)

randList2.sort()
#randList2.reverse()
randList2.insert(5,10)
randList2.remove(10)
randList2.pop(2)


for k in randList2:
    print(k, end=", ")
print()

#####################################

#List comprehension

evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)

numList = [1,2,3,4,5]

listOfvalues = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)]
                for m in numList]

for i in listOfvalues:
    print(i)
print()

multiDList = [[0]* 10 for i in range(10)]

multiDList[0][1] = 10

print(multiDList[0][1])

listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()

###########

###########PROBLEM 3###############
print()
multiplication_List = [[i*i] * 10 for i in range(10)]
for i in range(1,10):
    for j in range(1,10):
        multiplication_List[i][j] = i*j

for i in range(1,10):
    for j in range(1,10):
        print(multiplication_List[i][j], end=" || ")
    print()

####################################