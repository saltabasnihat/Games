import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

config = ConfigParser()
config.add_section('mysql')
config.set('mysql', 'host', 'localhost')
config.set('mysql', 'user', 'abc')
config.set('mysql', 'password', '1234')
config.set('mysql', 'database', 'Student')

with open('config.ini', 'w') as config_file:
    config.write(config_file)

# The purpose of this lab is to interact with a mySql database on a remote server via a local python program.
def readDBConfig(filename='config.ini', section='mysql'):
    db = {}

    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        print('Error with config.ini file')
    return db

print(readDBConfig())

def InsertGrade(LName, FName, Province, Grade):
    try:
        config = readDBConfig()
        mariadb = mysql.connector.connect(**config)
        cursor = mariadb.cursor()
        sql = "INSERT INTO grades (LName, FName, Province, Grade) VALUES (%s, %s, %s, %s)"
        values = (LName, FName, Province, Grade)
        cursor.execute(sql, values)
        mariadb.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as error:
        print("Failed to insert record into table: {}".format(error))
    finally:
        cursor.close()
        mariadb.close()

def DeleteGrade(LName, FName, Province, Grade):
    try:
        config = readDBConfig()
        mariadb = mysql.connector.connect(**config)
        cursor = mariadb.cursor()
        sql = "DELETE FROM grades WHERE LName = %s AND FName = %s AND Province = %s AND Grade = %s"
        values = (LName, FName, Province, Grade)
        cursor.execute(sql, values)
        mariadb.commit()
        print("Record deleted successfully")
    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        cursor.close()
        mariadb.close()


def DisplayGrade(LName, FName, Province):
    try:
        config = readDBConfig()
        mariadb = mysql.connector.connect(**config)
        cursor = mariadb.cursor()
        sql = "SELECT Grade FROM grades WHERE LName LIKE %s AND FName LIKE %s AND Province LIKE %s"
        values = ('%' + LName + '%', '%' + FName + '%', '%' + Province + '%')
        cursor.execute(sql, values)
        results = cursor.fetchall()
        cursor.close()
        mariadb.close()
        return [row[0] for row in results]
    except mysql.connector.Error as error:
        print("Failed to retrieve grades from table: {}".format(error))
        return []


def Main():
    while True:
        print("\nStudent Grade Database")
        print("1. Please Insert a grade")
        print("2. Please Display a grade")
        print("3. Please Delete a grade")
        print("4. Exit")

        choice = input("Enter one of the options (1-4): ")

        if choice == "1":
            LastName = input("Please last name: ")
            FName = input("Please first name: ")
            Province = input("Enter province: ")
            Grade = input("Enter grade: ")
            InsertGrade(LastName, FName, Province, Grade)

        elif choice == "2":
            LName = input("Please last name: ")
            FName = input("Please first name: ")
            Province = input("Enter province: ")
            grades = DisplayGrade(LName, FName, Province)
            print("Grades:")
            for grade in grades:
                print(grade)

        elif choice == "3":
            LName = input("Please last name: ")
            FName = input("Please first name: ")
            Province = input("Enter province: ")
            Grade = input("Enter grade: ")
            DeleteGrade(LName, FName, Province, Grade)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Wrong!!! Enter a number between 1 and 4.")

Main()
