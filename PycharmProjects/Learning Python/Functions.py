def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 =",add_numbers(5,4))


########GLOBAL VARIABLES##############

'''
def assign_name():
    name = "Doug"

assign_name()

print(name)

'''

global_name = "Sally"

def change_name():
    global global_name
    global_name = "Sammy"

#name = "Tom"

change_name()

print(global_name)

########Functions not returning anything return NONE as Default

#############PROBLEM 1#####################

#Solve for x
# x+4=9
#x will always be 1st value recieved and you only will deal with addition

def solve(equation):
    x, add, num1, equal, num2 = equation.split()
    num1 , num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)

print(solve("x + 4 = 9"))


#How to return multiple values

def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5,4)

print("5 * 4 =", mult,"||", "5 / 4 =", divide)


#How to return a list

#a prime can only be divided by 1 and itself

def isPrime(num):
    for i in range(2, num):
        if(num % i) == 0:
            return False

    return True

def getPrimes(max_num):

    list_of_primes = []

    for num1 in range(2, max_num):
        if isPrime(num1):
            list_of_primes.append(num1)

    return list_of_primes

max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)


#Unknown number of arguments received into an argument

def sumAll(*numbers):
    sum = 0

    for number in numbers:
        sum += number

    return sum

print("Sum : ", sumAll(1,2,3,4,5,6,7,8,9,10))


#SOme bigger functions
#Calculating areas

import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))
    area = length * width
    print("The area of rectangle is", area)

def circle_area():
    radius = float(input("Enter the radius : "))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is {:.2f}".format(area))

def main():
    shape_type = input("Get area for what shape : ")

    get_area(shape_type)


main()