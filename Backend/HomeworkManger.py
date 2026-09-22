import os
import sqlite3

# Convert reltive path to aboslute
ReltivePath = "Data/Homework.db"
AbsolutePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),ReltivePath)
# print(AbsolutePath)

# # Create Table - id, Task, Due Date, Notes, Subject, status, prioritry
# cursor.execute("""
#     CREATE TABLE Homework(
#         id INTERGER PRIMARY KEY,
#         Task TEXT NOT NULL,
#         DueDate DATETIME,
#         Notes TEXT,
#         Subject TEXT,
#         status TEXT,
#         priority TEXT
#     )
#     """)

class HomeworkManger:
    def __init__(self, Path):
        self.path = Path

    def AddHomework (self, Task, DueDate = None, Notes = None, Subject = None, Status = None, Priority = None):
        # Connection to Database
        conn = sqlite3.connect(self.path)

        # Create cursor in the database
        cursor = conn.cursor()

        # Insert Data into the Table
        cursor.execute("""
            INSERT INTO Homework
            (Task, DueDate, Notes, Subject, Status, Priority)
            VALUES(?,?,?,?,?,?)
            """ , (Task, DueDate, Notes, Subject, Status, Priority))

        # Commit changes
        conn.commit()

        # Close the connection to the database
        conn.close()

    def AlterHomework (self, Task, DueDate = None, Notes = None, Subject = None, Status = None, Priority = None):
        # Connection to Database
        conn = sqlite3.connect(self.path)

        # Create cursor in the database
        cursor = conn.cursor()

        # Insert Data into the Table
        cursor.execute("""
            INSERT INTO Homework VALUES(?,?,?,?,?,?)
            """ , [(Task, DueDate, Notes, Subject, Status, Priority)])

        # Commit changes
        conn.commit()

        # Close the connection to the database
        conn.close()

if "__main__" == __name__:
    # Connection to Database
    conn = sqlite3.connect(AbsolutePath)

    # Create cursor in the database
    cursor = conn.cursor()

    # Make a query to the Database
    cursor.execute("SELECT * FROM Homework")

    # Fetch the data form query
    print(cursor.fetchall())

    # Commit changes
    conn.commit()

    # Close the connection to the database
    conn.close()
