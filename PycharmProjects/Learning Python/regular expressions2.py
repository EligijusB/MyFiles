import re

# Did you find a match
# if re.search("REGEX", yourString)

# Get list of matches
# print("Matches :", len(re.findall("REGEX", yourString)))

# Get a pattern object
# regex = re.compile("REGEX")

# Substitute the match
# yourString = regex.sub("substitution", yourString)

# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length

# ---------- Matching Zero or One ----------

randStr = "cat cats"

regex = re.compile("[cat]+s?") # ? 0 or 1

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

randStr2 = "doctor doctors doctor's"

regex2 = re.compile("[doctor]+['s]*") # ? 0 or more

matches2 = re.findall(regex2, randStr2)

for i in matches2:
    print(i)

print()

randStr3 = '''Just some words
and some more\r
and more
'''

regex3 = re.compile("[\w\s]+[\r]?\n") # ? 0 or 1

matches3 = re.findall(regex3, randStr3)

for i in matches3:
    print(i)

randStr4 = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

regex4 = re.compile("<name>(.*?)</name>") #making * not greedy

matches4 = re.findall(regex4, randStr4)

for i in matches4:
    print(i)

print()

randStr5 = "ape at the apex"

regex5 = re.compile(r"\bape\b") # setting boundaries

matches5 = re.findall(regex5, randStr5)

for i in matches5:
    print(i)


print()

#^ : beginning of string
#$ : end of the string

randStr6 = "match everything up to @"

regex6 = re.compile(r"^.*[^@]") # string boundaries

matches6 = re.findall(regex6, randStr6)

for i in matches6:
    print(i)

print()

randStr7 = "@ Get this string"

regex7 = re.compile(r"[^@\s].*$") # setting boundaries

matches7 = re.findall(regex7, randStr7)

for i in matches7:
    print(i)

print()

randStr8 = '''Ape is big
Turtle is slow
Cheetah is fast
'''

regex8 = re.compile(r"(?m)^.*?\s") # multi line code

matches8 = re.findall(regex8, randStr8)

for i in matches8:
    print(i)

randStr9 = "My number is 412-555-1212"

regex9 = re.compile(r"412-(.*)") # multi line code

matches9 = re.findall(regex9, randStr9)

for i in matches9:
    print(i)