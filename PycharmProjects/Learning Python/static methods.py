##allows access without the need to create a class
# utility methods

class Sum:

    @staticmethod
    def getSum(*args): #using splat

        sum = 0

        for i in args:
            sum+=i

        return sum

class Dog:
    num_of_dogs = 0 #static variable shared by every dog variable

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    print("Sum :", Sum.getSum(1,2,3,4,5))
    print()

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()
main()