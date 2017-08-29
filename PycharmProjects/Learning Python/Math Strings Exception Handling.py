import math
from decimal import Decimal as D

'''
while True:

    try:
        number = int(input("Please enter a number : "))
        break

    except ValueError:
        print("You didnt enter a number")

    except:
        print("An unknown error occurred")



print("Thank you for entering a number")

#PROBLEM GUESS A NUMBER

number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if(guess == number):
        print("You guessed it")
        break


print("ceil(4.4) = ", math.ceil(4.4)) # round up
print("floor(4.4) = ", math.floor(4.4)) # round down
print("fabs(-4.4) = ", math.fabs(-4.4)) # round up

#factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4)) # factorial function

#Return a remainder of a devision
print("fmod(4.4) = ", math.fmod(5,4)) #remainder of devision

#Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2)) # get float return int

#Return x^y
print("pow(2,2) = ", math.pow(2,2)) # x to the power of y

#Return the square root
print("sqrt(4) = ", math.sqrt(4)) # return square root

#Spacial values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

#Return e^x
print("exp(4) = ", math.exp(4))

#Return natural logarithm e * e * e ~= 20 so log(20) tells you that e^3 ~= 2=
print("log(20) = ", math.log(20))

#You can define the base and 10^3 = 1000
print("log(1000, 10) = ", math.log(1000,10))

#You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))



#Decimal modules performing more accurate float calculations

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum =" ,sum)

print(".1 + .1 + .1 - .3 = ", .1 + .1 + .1 - .3 )

'''
#creating strings

samp_stirng = "This is a very important string"

print(samp_stirng[0])
print(samp_stirng[-1])
print(samp_stirng[3+5])

print("Length : ", len(samp_stirng))

print(samp_stirng[0:4])
print(samp_stirng[8:])
print("Green " + "Eggs")
print("Hello " * 5)

num_string = str(4)

for char in samp_stirng:
    print(char)

for i in range(0, len(samp_stirng)-1, 2):
    print(samp_stirng[i] + samp_stirng[i+1])


#A - Z 65 - 90
#a - z 97 - 122

print("A = ", ord("A"))
print("65 = ", chr(65))

###################PROBLEM####################

#Enter a string to hide in uppercase:
message = input("Enter a message in UPPERCASE: ")

#Secret Message :
print("Secret Message: ", end="")
secret_message = ""
for char in message:
    print(ord(char), end="")
    secret_message += str(ord(char) - 23)
print()
#Original Message :
original_string = ""

for i in range(0, len(secret_message), 2):
    char_code = secret_message[i] + secret_message[i+1]

    original_string += chr(int(char_code) + 23)
print("Original Message: ", original_string)