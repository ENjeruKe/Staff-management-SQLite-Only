#[START OF sqlClient.py]
#[SCRIPT_GENERATED AT {2024-10-04} {UTC+3}]
# SCRIPT DETAILS: sqlClient_SQLite_Version_20241004.py
#
# This script has been modified to use SQLite instead of MySQL. 
# SQLite database file is named "employees.db" and is located in the same folder as the main script.
#
#--------------------------------------------------------

import sqlite3
import os

class mySqlClient:  # Renaming kept for consistency, even though it now handles SQLite.

    def __init__(self, database: str = 'employees.db'):
        '''
        Initializes SQLite connection and cursor.
        Creates the employeeDetails table if it doesn't exist.
        :param database: Name of the SQLite database file. Default: 'employees.db'
        '''
        # Establish SQLite connection
        self.sqlClient = sqlite3.connect(database)
        self.cursor = self.sqlClient.cursor()

        # Create table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS employeeDetails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dateOfBirth TEXT,
            joiningDate TEXT,
            salary REAL,
            department TEXT
        );
        '''
        self.cursor.execute(create_table_query)
        self.sqlClient.commit()

    def insertEmployee(self, name: str, dateOfBirth: str, joiningDate: str, department: str, salary: float):
        '''
        Insert a new employee record into the employeeDetails table.
        :param name: Employee's full name (first and last)
        :param dateOfBirth: Employee's date of birth (format: yyyy-mm-dd)
        :param joiningDate: Date employee joined the organization (format: yyyy-mm-dd)
        :param salary: Employee's salary
        :param department: Employee's department
        '''
        insert_query = "INSERT INTO employeeDetails (name, dateOfBirth, joiningDate, salary, department) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(insert_query, (name, dateOfBirth, joiningDate, salary, department))
        self.sqlClient.commit()

    def findEmployee(self, method: str, value: str):
        '''
        Find employees based on method (Id/Name/Birth Date/Joining Date/Salary).
        :param method: Search method ('Id', 'Name', 'Birth Date', 'Joining Date', 'Salary')
        :param value: Value to search by
        :return: List of matching employees
        '''
        queries = {
            'Id': "SELECT * FROM employeeDetails WHERE id = ?",
            'Name': "SELECT * FROM employeeDetails WHERE name LIKE ?",
            'Birth Date': "SELECT * FROM employeeDetails WHERE dateOfBirth = ?",
            'Joining Date': "SELECT * FROM employeeDetails WHERE joiningDate = ?",
            'Salary': "SELECT * FROM employeeDetails WHERE salary = ?"
        }
        query = queries.get(method)
        if method == 'Id':
            self.cursor.execute(query, (int(value),))
        elif method == 'Name':
            self.cursor.execute(query, ('%' + value + '%',))
        else:
            self.cursor.execute(query, (value,))
        return self.cursor.fetchall()

    def deleteEmployee(self, method: str, value: str):
        '''
        Delete an employee record based on the method (Id/Name/Birth Date/Joining Date/Salary).
        :param method: Deletion method
        :param value: Value to search and delete by
        '''
        queries = {
            'Id': "DELETE FROM employeeDetails WHERE id = ?",
            'Name': "DELETE FROM employeeDetails WHERE name LIKE ?",
            'Birth Date': "DELETE FROM employeeDetails WHERE dateOfBirth = ?",
            'Joining Date': "DELETE FROM employeeDetails WHERE joiningDate = ?",
            'Salary': "DELETE FROM employeeDetails WHERE salary = ?"
        }
        query = queries.get(method)
        if method == 'Id':
            self.cursor.execute(query, (int(value),))
        elif method == 'Name':
            self.cursor.execute(query, ('%' + value + '%',))
        else:
            self.cursor.execute(query, (value,))
        self.sqlClient.commit()

    def updateEmployee(self, method: str, value: str, newValue: tuple):
        '''
        Update an employee record based on a method (Id/Name/Birth Date/Joining Date/Salary).
        :param method: Search method
        :param value: Value to search by
        :param newValue: New values to update (id, name, dateOfBirth, joiningDate, salary, department)
        '''
        queries = {
            'Id': "UPDATE employeeDetails SET name = ?, dateOfBirth = ?, joiningDate = ?, salary = ?, department = ? WHERE id = ?",
            'Name': "UPDATE employeeDetails SET name = ?, dateOfBirth = ?, joiningDate = ?, salary = ?, department = ? WHERE name LIKE ?",
            'Birth Date': "UPDATE employeeDetails SET name = ?, dateOfBirth = ?, joiningDate = ?, salary = ?, department = ? WHERE dateOfBirth = ?",
            'Joining Date': "UPDATE employeeDetails SET name = ?, dateOfBirth = ?, joiningDate = ?, salary = ?, department = ? WHERE joiningDate = ?",
            'Salary': "UPDATE employeeDetails SET name = ?, dateOfBirth = ?, joiningDate = ?, salary = ?, department = ? WHERE salary = ?"
        }
        query = queries.get(method)
        self.cursor.execute(query, (*newValue[1:], value))  # newValue[1:] for all values excluding id
        self.sqlClient.commit()

    def getAllEmployees(self):
        '''
        Retrieve all employee records from the database.
        :return: List of all employees
        '''
        query = "SELECT * FROM employeeDetails"
        self.cursor.execute(query)
        return self.cursor.fetchall()

#[END OF sqlClient.py]
