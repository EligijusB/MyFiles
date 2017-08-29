import random
import math
'''
Real world objects : attributes and capabilities

Dog attributes (fields/ variables) : height weight favorite food

Dog capabilities (methods and fuctions) : run walk eat
'''
'''
class Dog:

    #constructor
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


######getters and setters

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the Height")

        return self.__height

    @height.setter
    def height(self, value):
        if(value.isdigit()):
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width

    @width.setter
    def width(self, value):
        if (value.isdigit()):
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.height) * int(self.width)

def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()

    bowser = Dog()
    bowser.bark()

    aSquare = Square()

    height = input("Enter Height : ")

    width = input("Enter Width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)
    print("The Area is :", aSquare.getArea())


'''

class Warrior:

    def __init__(self, name = "Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmount = self.attkMax * (random.random() + 0.5)
        return attkAmount

    def block(self):
        blockAmount = self.blockMax * (random.random() + 0.5)
        return blockAmount


class Battle:

    def startFight(self, warrior1, warrior2):

        while True:

            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttackAmount = warriorA.attack()
        warriorBBlcokAmount = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttackAmount - warriorBBlcokAmount)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name,
                                                         damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"



def main():

    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)


main()