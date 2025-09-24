from flask import Blueprint, render_template, request
from db.DatabaseSingleton import get_databases


returnBlueprint = Blueprint("return_books", __name__)

database = get_databases()
books_collection = database['books']
students_collection = database['students']


@returnBlueprint.get("/return_books")
def return_books():
    return render_template("return_books.html")


@returnBlueprint.post("/print_return_books")
def print_return_books():
    student = request.form.get("student_id")
    student = int(student)
    pipeline = [
        {
            "$lookup": {
                "from": "students",
                "localField": "isbn",
                "foreignField": "isbn",
                "as": "borrowed_by"
            }
        },
        {
            "$unwind": "$borrowed_by"
        },
        {
            "$match": {
                "borrowed_by.Student ID": student
            }
        }
    ]

    books = list(books_collection.aggregate(pipeline))

    pagetitle = "Restituzione Libri"

    return render_template("new/selectable_list.html", pagetitle=pagetitle, books=books, student=student, show_matricola_field=False, action="/check_return_books")

@returnBlueprint.post("/check_return_books")
def check_return_books():
    student = request.form.get("student_id")
    selection_books_isbn = request.form.getlist("take_isbn")  # books

    students_collection.update_one(
        {"Student ID": int(student)},
        {"$pull": {"isbn": {"$in": selection_books_isbn}}}
    )

    for isbn in selection_books_isbn:
        books_collection.update_one(
            {"isbn": isbn},
            {"$inc": {"copy": 1}}
        )

    titles = []
    for isbn in selection_books_isbn:
        libro = books_collection.find_one({"isbn": isbn}, {"title": 1, "_id": 0})
        if libro and "title" in libro:
            titles.append(libro["title"])

    return render_template("check_return_books.html", titles=titles, student=student)



