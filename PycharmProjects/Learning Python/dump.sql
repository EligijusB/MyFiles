BEGIN TRANSACTION;
CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary Real, HireDate TEXT, 'Image' BLOB DEFAULT NULL);
INSERT INTO "Employees" VALUES(1,'Eligijus','Blankus',20,'121 Main St',50000.0,'2017-08-16',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Employees',1);
COMMIT;
