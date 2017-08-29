import random
import sys
import os

print("Hello World")

name = "Derek"
print(name)

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

quote = "\"Always remember you are unique"

multi_line_quote = '''Just like everyone
else'''

newString = quote + multi_line_quote

print("%s %s %s" % ('I like the quote' , quote, multi_line_quote))

print("I dont like " , end="")
print("newlines")

#Comment

'''
this 
is 
a 
milti 
line
comment
'''