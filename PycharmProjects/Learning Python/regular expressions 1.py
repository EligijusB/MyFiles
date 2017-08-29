import re #regular expression module

if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

allApes = re.findall("ape.", "The ape was at the apex") ## "." used to match any one char or space

for i in allApes:
    print(i)

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):

    locTuple = i.span()

    print(locTuple)

    print(theStr[locTuple[0]:locTuple[1]])


#match one of any of several letters

animalStr = "Cat rat mat pat"

allAnimals = re.findall("[Crmfp]at", animalStr)

for i in allAnimals:
    print(i)

someAnimals = re.findall("[c-mC-M]at", animalStr) #specifying range of chars

for i in someAnimals:
    print(i)
print()
someAnimals2 = re.findall("[^Cr]at", animalStr) #specifying anything but char in range

for i in someAnimals2:
    print(i)

#replacing strings
print()

owlFood = "rat cat mat pat"

regex = re.compile("[cr]at")

owlFood = regex.sub("owl", owlFood)

print(owlFood)

#backslash problems
print()

randStr = "Here is \\stuff"

print("Find \\stuff :", re.search(r"\\stuff", randStr)) #using r in front of string

#finding periods
print()

randStr2 = "F.B.I I.R.S. CIA"

print("Matches :", len(re.findall(".\..\.", randStr2)))

#finding white space
print()

randStr3 = '''This is a long
string that goes
on for many lines'''

print(randStr3)

regex = re.compile("\n")

randStr3 = regex.sub(" ", randStr3)

print(randStr3)

# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab


# You may need to remove \r\n on Windows

# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]
print()

randStr4 = "12345"

print("Matches :", len(re.findall("\d{2}", randStr4)))

randStr5 = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", randStr5)))

# ---------- Matching Any Single Letter or Number ----------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]
print()

phNum = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("it is a phone number")

if re.search("\w{2,20}", "Ultranam"):
    print("Valid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}", "Toshio Maramutsu"):
    print("It is valid")

print("Matches :", len(re.findall("a+", "a as ape bug")))


##PROBLEM###
# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = " db@aol.com m@.com @apple.com db@.com eat@email.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
                                        emailList)))
















