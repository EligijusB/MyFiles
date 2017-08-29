import sqlite3
import sys

def printDB():

    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, "
                                   "Salary, HireDate FROM Employees")

        for row in result:
            print("ID :", row[0])
            print("Name :", row[1])
            print("Surname :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
    except sqlite3.OperationalError:
        print("ERROR OCCURRED")

db_connect = sqlite3.connect("test.db")

print("Database Created")

theCursor = db_connect.cursor()
db_connect.execute("DROP TABLE IF EXISTS Employees")
db_connect.commit()

try:

    db_connect.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY "
                       "AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, "
                       "LName TEXT NOT NULL, Age INTEGER NOT NULL, "
                       "Address TEXT, Salary Real, HireDate TEXT);")

    db_connect.commit()


except sqlite3.OperationalError:
    print("Table couldn't be created")

print("Table created")

db_connect.execute("INSERT INTO Employees (FName, LName, Age, Address, "
                   "Salary, HireDate) VALUES ('Eligijus', 'Blankus', 20, "
                   "'801a Romford Road', 50000, date('now'))")

db_connect.commit()

printDB()

try:
    db_connect.execute("UPDATE Employees SET Address = '121 Main St' WHERE ID=1")
    db_connect.commit()

except sqlite3.OperationalError:
    print("Table couldn't be updated")

printDB()


#deleting individual rows
'''
try:
    db_connect.execute("DELETE FROM Employees WHERE ID=1")
    db_connect.commit()
except sqlite3.OperationalError:
    print("Info couldn't be deleted")

printDB()

db_connect.rollback()
'''
try:
    db_connect.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL")
    db_connect.commit()

except sqlite3.OperationalError:
    print("Table couldn't be updated")

theCursor.execute("PRAGMA TABLE_INFO(Employees)")

rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]

print(rowNames)

theCursor.execute("SELECT COUNT(*) FROM Employees")
numOfRows = theCursor.fetchone()

print("Total Rows :", numOfRows)

with db_connect:
    db_connect.row_factory = sqlite3.Row
    theCursor = db_connect.cursor()
    theCursor.execute("SELECT * FROM Employees")
    rows = theCursor.fetchall()

    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))

with open("dump.sql", "w") as f:
    for line in db_connect.iterdump():
        f.write("%s\n" % line)

db_connect.close()

print("Database Closed")
