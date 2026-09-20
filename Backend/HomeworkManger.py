import json

HomeworkFile = "Backend/Data/Homework.json"

with open(HomeworkFile, "r") as file:
    HomeworkData = json.load(file)
data = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phone": "9976770500"
}

HomeworkData["Due"].append(data)

with open(HomeworkFile, "w") as file:
    json.dump(HomeworkData, file, indent=16)
