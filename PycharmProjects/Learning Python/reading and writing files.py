import os
'''
with open("mydata.txt", mode = "w", encoding = "utf-8") as myFile:
    myFile.write("Some random text\n<pre ramdon text\nSome more")

with open("mydata.txt", encoding="utf-8") as myFile:
    # read() ----------- reads everything into one string up to it gets to new line

    # readline() ---------- reads everything into one string including new line

    #readLines() ----------- returns a list of every line which includes all new lines

    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

#os.mkdir("mydir")

os.chdir("mydir")

print("Current Directory :", os.getcwd())

os.chdir("..")

print("Current Directory :", os.getcwd())

os.rmdir("mydir")
'''

'''
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result


# Ask how many numbers they want
number_count = int(input("How many fibinochi numbers you want? : "))

# Loop while calling for each new number
i = 1
while i <= number_count:
    print(fib(i))
    i += 1

print("All Done!")
'''

#####HOW to read whole document line by line########
with open("mydata2.txt", mode = "w", encoding = "utf-8") as myFile:
    myFile.write("Some random text\n<pre ramdon text\nSome more")

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum)
        word_list = line.split()
        numberOfwords = len(line.split())
        print("Number of Words :", len(word_list))

        charCount = 0

        for word in word_list:
            for char in word:
                charCount += 1

        avgNumChars = charCount/numberOfwords

        print("Avg Word Length : {:.2}".format(avgNumChars))
        lineNum += 1


###########Looking at tuples############

myTuple = (1,2,3,4,5,8)

print("1st value :", myTuple[0])

print(myTuple[0:3])

print("Tuple Length :", len(myTuple))

moreFibs = myTuple + (13,21,34)

print("34 in Tuple :", 34 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55, 89, 44]
aTuple = tuple(aList)

aList = list(aTuple)

print("Min :", min(aTuple))
print("Max :", max(aTuple))