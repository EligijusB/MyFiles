


rand_string = "        this is an important string      "

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

print(rand_string.capitalize())

print(rand_string.upper())

print(rand_string.lower())

a_list = ["Buch", "of", "random", "words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)

print("how many is :", rand_string.count("is"))

print("where is string :", rand_string.find("string"))

print(rand_string.replace("an ", "a kind of "))



#############PROBLEM 1################

# Random Access Memory : RAM

string_to_convert = input("Enter a string: ")

word_list = string_to_convert.split()

acronym = ""

for word in word_list:
    acronym += word[0].upper()

print(acronym)



###########PROBLEM 2################

letter_z = "z"
num_3 = "3.14"
a_space = " "

print("Is z a letter or number : ", letter_z.isalnum())

print("Is z a letter : ", letter_z.isalpha())

print("Is 3 a number : ", num_3.isdigit())

print("Is z lowercase : ", letter_z.islower())

print("Is z uppercase : ", letter_z.isupper())

print("Is space a space : ", a_space.isspace())

def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

print("Is PI a float : ", isFloat(num_3))


##################PROBLEM 3####################

#A - Z 65-90
#a - z 97-122
#unicode ord(letter)
#character chr(unicode)


message = input("Enter your message : ")
key = int(input("How many characters should we shift (1-26)"))

secret_message = ""

for char in message:

    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if(char_code > ord("Z")):
                char_code -= 26

            if char_code < ord("A"):
                char_code += 26

    else:
        if char.isupper():
            if (char_code > ord("z")):
                char_code -= 26

            if char_code < ord("a"):
                char_code += 26

    secret_message += chr(char_code)

else:
    secret_message += char

print("Encrypted : ", secret_message)


key = -key
original_message = ""

for char in secret_message:

    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if(char_code > ord("Z")):
                char_code -= 26

            if char_code < ord("A"):
                char_code += 26

    else:
        if char.isupper():
            if (char_code > ord("z")):
                char_code -= 26

            if char_code < ord("a"):
                char_code += 26

    original_message += chr(char_code)

else:
    original_message += char

print("Original : ", original_message)















