from ctypes.util import test
from datetime import datetime

from HomeworkManger import *

due_date = datetime.strptime("2026-11-29 12:01", "%Y-%m-%d %H:%M").astimezone()

print(due_date)

Test = HomeworkManger(AbsolutePath)
Test.AddHomework("Kill", due_date, "Him", "Hitman", "Not Done", "Low")
