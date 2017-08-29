# iterable is an object with a method __iter__

#iterator is an object witha  method __next__

sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))


class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

alpha = Alphabet()

for letter in alpha:
    print(letter)


derek = {"fName":"Derek", "lName":"Banas"}

for key in derek:
    print(key, derek[key])


###list comprehension

print(list(map((lambda x: x * 2), range(1, 11))))

##list comprehension

print([2 * x for x in range(1,11)])

print(list(filter((lambda x: x%2 != 0), range(1,11))))

print([x for x in range(1,11) if x % 2 != 0])

#generate 50values take to the power of 2 return multiples of 8
print([x**2 for x in range(1, 51) if x%8 == 0])

#multiple for loops

print([x * y for x in range(1, 3) for y in range(11, 16)])

#generate a list of 10 values
#multiply them by 2
#return multiples of 8

print([x for x in [i * 2 for i in range(10)] if x%8==0])

#######PROBLEM 1###########
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension
# This is a hard one!
import random

print([x for x in [random.randint(1,1001) for i in range(50)] if x % 9 == 0])

multList = [[1,2,3],
            [4,5,6],
            [7,8,9]]

print([col[1] for col in multList])

print([multList[i][i] for i in range(len(multList))])

##generator functions

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isPrime(num1):
            yield num1

prime = gen_primes(50)

print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))

# generator expressions
#return results one of the time

double = (x * 2 for x in range(10))

print("Double :", next(double))
print("Double :", next(double))
print("Double :", next(double))
print("Double :", next(double))

for num in double:
    print(num)