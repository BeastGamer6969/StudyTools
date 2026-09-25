import random

from HomeworkManger import *


def RandomData(NumberOfData, object):
    Tasks = [
        "Complete maths homework",
        "Study for science test",
        "Finish English assignment",
        "Complete programming task",
        "Read history chapter",
        "Work on project",
        "Finish worksheet",
        "Revise notes"
    ]
    DueDates = [
        "2026-09-25 15:00:00",
        "2026-09-26 17:00:00",
        "2026-09-27 12:00:00",
        "2026-09-28 15:30:00",
        "2026-09-29 18:00:00"
    ]
    Notes = [
        "Finish all questions",
        "Review class notes first",
        "Ask teacher if stuck",
        "Complete before the weekend",
        "Check answers before submitting",
        ""
    ]
    Subjects = [
        "Maths",
        "English",
        "Science",
        "Software Engineering",
        "History",
        "Industrial Technology"
    ]
    Statuses = [
        "Not Done",
        "In Progress",
        "Done"
    ]
    Priorities = [
        "Low",
        "Medium",
        "High"
    ]

    for i in range(NumberOfData):
        Task = random.choice(Tasks)
        DueDate = random.choice(DueDates)
        Note = random.choice(Notes)
        Subject = random.choice(Subjects)
        Status = random.choice(Statuses)
        Priority = random.choice(Priorities)

        object.Addvalue(Task, DueDate, Note, Subject, Status, Priority)

Test = DatabaseManger(AbsolutePath)
# RandomData(10, Test)
Test.DeleteValues(1)
