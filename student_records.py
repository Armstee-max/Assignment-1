import json


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    score = int(input("Enter score: "))

    student = {
        "name": name,
        "age": age,
        "course": course,
        "score": score
    }
    return student

students = []

def save_students():
    student = add_student()
    students.append(student)
    with open("students.json", "w") as file:
        json.dump(students, file)

def load_students():
    with open("students.json", "r") as file:
        load = json.load(file)
        return load



def display_students():
    students = load_students()
    print("Student Records:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Score: {student['score']}")


while True:
    print("STUDENTS RECORD SYSTEM")
    print("1. Add students")
    print("2. View students")
    print("3. Exit")

    decision = input("Enter your choice: ")

    if decision == "1":
        save_students()
    elif decision == "2":
        display_students()
    elif decision == "3":
        break