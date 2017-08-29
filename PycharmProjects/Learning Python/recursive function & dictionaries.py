# dictionaries use key : value pairs

eligijusDictionary = {"Fname" : "Eligijus",
                      "Sbane" : "Blankus",
                      "Address" : "801a Romford Road"}

print("My Name :", eligijusDictionary["Fname"])

eligijusDictionary["Address"] = "New Address"

eligijusDictionary['city'] = 'Pittsburgh'

print("Is there a city :", "city" in eligijusDictionary)

print(eligijusDictionary.values())

print(eligijusDictionary.keys())

for k,v in eligijusDictionary.items():
    print(k,v)

print(eligijusDictionary.get("Sbane", "Not Here"))

del eligijusDictionary["Sbane"]

for i in eligijusDictionary:
    print(i)

eligijusDictionary.clear()

employees = []

#fName , lName = input("Enter Employee Name :").split()

#employees.append({"fName" : fName, "lName" : lName})

#print(employees)

#####################PROBLEM 1######################
employees2 = []

while True:
    userMsg = input("Enter Customer (Yes/No) : ")
    if userMsg == "Yes" or userMsg == "y" or userMsg == "Y" or userMsg == "yes":
        fName, lName = input("Enter Customer Name : ").split()
        employees2.append({"fName" : fName, "lName" : lName})
        continue;
    elif userMsg == "No" or userMsg == "n" or userMsg == "N" or userMsg == "no":
        for dict in employees2:
            print(dict["fName"], dict["lName"] )
        break
    else:
        break

######################################################

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

print(factorial(4))