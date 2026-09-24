from datetime import datetime

from HomeworkManger import *

due_date = datetime.strptime("2026-11-29 12:01", "%Y-%m-%d %H:%M").astimezone()

print(due_date)

Test = DatabaseManger(AbsolutePath)
Test.AddHomework("not Kill", due_date, "Him", "Hitman", "Not Done", "Low")
