from flask import Blueprint, render_template, request
from config.config import get_databases

studentsBlueprint = Blueprint("students", __name__)

get_databases = get_databases()
students = get_databases["students"]

@studentsBlueprint.post("/insert_students")
def insert_students():
    return render_template("insert_students.html")

@studentsBlueprint.post("/add_student")
def add_student():

    student_id = int(request.form["student_id"])
    name = request.form["name"]
    gender = request.form["gender"]
    age = int(request.form["age"])
    major = request.form["major"]
    interested_domain = request.form["interested_domain"]

    # check student_id
    existing_student = students.find_one({"Student ID": student_id})

    if existing_student:
        error_message = f"Errore: Uno studente con Matricola '{student_id}' esiste già."
        return render_template("error/error_insert_student.html", error_message=error_message)

    new_student = {
        "Student ID": student_id,
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Major": major,
        "Interested Domain": interested_domain
    }

    students.insert_one(new_student)


    return render_template("add_students.html", new_student=new_student)