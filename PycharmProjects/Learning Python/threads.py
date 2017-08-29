import threading
import time
import random

'''
def executeThread(i):
    print("Thread {} sleeps at {}".format(i,
                                          time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1,5)

    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at {}".format(i,
                                          time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads :", threading.active_count()) ##prints out num of threads that are currently executing

    print("Thread Objects :", threading.enumerate()) ## returns a list of all active threads
'''

#subclassing a thread
'''
class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Execution Ends")

def getTime(name):
    print("Thread {} starts sleeping at {}".format(name,
                time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)

thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive :", thread1.is_alive())
print("Thread 2 Alive :", thread2.is_alive())

print("Thread 1 Name :", thread1.getName())
print("Thread 2 Name :", thread2.getName())

thread1.join()
thread2.join()

print("Execution Ends")
'''

#locking threads

class BankAccount(threading.Thread):

    acctBalance = 100

    def __init__(self, name, moneyRequested):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequested = moneyRequested

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name, customer.moneyRequested,
                                                      time.strftime("%H:%M:%S"), time.gmtime()))

        if BankAccount.acctBalance - customer.moneyRequested > 0:
            BankAccount.acctBalance -= customer.moneyRequested
            print("New account balance : ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

        time.sleep(3)

threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print("Execution Ends")