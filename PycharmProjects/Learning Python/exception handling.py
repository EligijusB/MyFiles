try:
    aList = [1, 2, 3]

    print(aList[3])

except(IndexError, NameError): # catching multiple exceptions
    print()
except IndexError:
    print("Sorry that index doesn't exist")

except:
    print("An unknown error occurred")


class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):

        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")


##execute code weather or not error occured

num1, num2 = input("Enter 2 values to divide : ").split()

try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("You didn't raise an exception")
finally:
    print("i execute no matter what")


#####PROBLEM 1


#create a file named mydata2.txt
#use what you learned in part 8 to find out how to open file without with(open in try)
#catch file not found error
#in else print contents
# in finally
# try to open non existent file mydata3.txt

try:
    myFile = open("mydata3.txt", mode="r", encoding="utf-8")

except FileNotFoundError as ex:
    print("File was not found")
    print(ex.args)

else:

    print(myFile.read())
    myFile.close()
finally:
    print("Finished working with file")
