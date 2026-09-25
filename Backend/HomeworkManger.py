import os
import sqlite3
from pathlib import Path

# Convert relative path to absolute
RelativePath = "Data/Homework.db"
AbsolutePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),RelativePath)
# print(AbsolutePath)

class DatabaseManger:
    def __init__(self, path):
        self.path = path
        self.Name = Path(path).stem

    def Addvalue (self, Task, DueDate = None, Notes = None, Subject = None, Status = None, Priority = None):
        # Connection to Database
        conn = sqlite3.connect(self.path)

        # Create cursor in the database
        cursor = conn.cursor()

        # Insert Data into the Table
        cursor.execute(f"""
            INSERT INTO {self.Name}
            (Task, DueDate, Notes, Subject, Status, Priority)
            VALUES(?,?,?,?,?,?)
            """ , (Task, DueDate, Notes, Subject, Status, Priority))

        # Commit changes
        conn.commit()

        # Close the connection to the database
        conn.close()

    def _AlterValue (self, Id, ColoumName, Value):
        # Connection to Database
        conn = sqlite3.connect(self.path)

        # Create cursor in the database
        cursor = conn.cursor()

        # Cammand to run in the database
        Cammand = f"""
            UPDATE {self.Name}
            SET {ColoumName} = '{Value}'
            WHERE id = {Id}
            """
        # Print the cammand - Debug
        print(Cammand)

        # Update Data in the Table
        cursor.execute(Cammand)

        # Commit changes
        conn.commit()

        # Close the connection to the database
        conn.close()

    def AlterValues (self, Id, Task=None, DueDate = None, Notes = None, Subject = None, Status = None, Priority = None):
        if Task != None:
            self._AlterValue(Id, "Task", Task)

        if DueDate != None:
            self._AlterValue(Id, "DueDate", DueDate)

        if Notes != None:
            self._AlterValue(Id, "Notes", Notes)

        if Subject != None:
            self._AlterValue(Id, "Subject", Subject)

        if Status != None:
            self._AlterValue(Id, "Status", Status)

        if Priority != None:
            self._AlterValue(Id, "Priority", Priority)

    def DeleteValues (self, Id):
        # Connection to Database
        conn = sqlite3.connect(self.path)

        # Create cursor in the database
        cursor = conn.cursor()

        # Insert Data into the Table
        cursor.execute(f"DELETE from {self.Name} Where id = {Id}")

        # Commit changes
        conn.commit()

        # Close the connection to the database
        conn.close()





















if "__main__" == __name__:
    # Connection to Database
    conn = sqlite3.connect(AbsolutePath)

    # Create cursor in the database
    cursor = conn.cursor()

    # # Delete the Homework table
    # cursor.execute("DROP TABLE Homework")

    # # Create Table - id, Task, Due Date, Notes, Subject, status, prioritry
    # cursor.execute("""
    #     CREATE TABLE Homework(
    #         id INTEGER PRIMARY KEY,
    #         Task TEXT NOT NULL,
    #         DueDate DATETIME,
    #         Notes TEXT,
    #         Subject TEXT,
    #         status TEXT,
    #         priority TEXT
    #     )
    #     """)

    # Make a query to the Database
    cursor.execute("SELECT * FROM Homework")

    # Fetch the data form query
    items = cursor.fetchall()
    for item in items:
        print(f"{item}\n")

    # Close the connection to the database
    conn.close()
