def mult_by_2(num):
    return num * 2

def do_math(func, num): ####passing in functions as parameters
    return func(num)

def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by ###returning a function which was created inside another function

generated_func = get_func_mult_by_num(5)
time_two = mult_by_2 ###assigning a function to a variable

listOfFuncs = [time_two, generated_func] ##storing functions inside a data structure

print("5 * 9 =", listOfFuncs[1](9))


print("4 * 2 =", time_two(4))

print("8 * 2 =", do_math(time_two, 8))

print("5 * 10 =", generated_func(10))


# ---------- PROBLEM ----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):

    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)

    return oddList

aList = range(1, 20)

print(change_list(aList, is_it_odd))

print()


###FUNCTION ANNOTATIONS#####

def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return"{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))

print(random_func(89, "Derek", "Turtle"))

print(random_func.__annotations__)


####ANNONYMOUS FUNCTIONS#####

#lambda arg1, arg2, .... : expression use the args

sum = lambda x, y: x + y

print("Sum :", sum(4,5))

can_vote = lambda age: True if age>= 18 else False

print("Can Vote :", can_vote(17))

power_list = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4] # storing lambda in list

for func in power_list:
    print(func(4))

attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Missed Attack"))}  ### storing lambda functions from dictionaries

attack['quick']()

import random
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

####PROBLEM 2#####

# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads :  46
# Tails :  54

flipList = []

for i in range(100):
    flipList.append(random.choice(['H', 'T']))

print("Heads :", flipList.count('H'))
print("Tails :", flipList.count('T'))


####MAP FUNCTION###
##allows to execute a function on each item in a list

oneTo10 = range(1,11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y: x+y), [1,2,3],[1,2,3]))

print(aList)

##Filter function###
# select item off of a list based on a function

print(list(filter((lambda x: x % 2 == 0), range(1,11))))

# ---------- PROBLEM ----------
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000
rangeList = list(random.randrange(1,1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), rangeList)))


###USING REDUCED###
# receive a list return a single result

from functools import reduce

print(reduce((lambda x,y: x+y), range(1,6)))
