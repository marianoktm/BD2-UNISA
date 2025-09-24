from flask import Blueprint, render_template, request
from db.DatabaseSingleton import get_databases

borrowBlueprint = Blueprint("borrowBooks", __name__)

databases = get_databases()
books_collection = databases["books"]
students_collection = databases["students"]


@borrowBlueprint.get("/borrow_books")
def borrow_books():
    books_cursor = databases['books'].find({"copy": {"$gt": 0}})

    books = list(books_cursor)

    pagetitle = "Prestito Libri"

    return render_template('new/selectable_list.html', books=books, pagetitle=pagetitle, action="/take_books", show_matricola_field=True)

@borrowBlueprint.post("/take_books")
def handler_borrow_books():
    selection_books_isbn = request.form.getlist("take_isbn") # books
    titles = []

    student = request.form.get("student_id")
    student_doc = students_collection.find_one({"Student ID": int(student)})

    if len(selection_books_isbn) >= 5:
        error_message = f"Errore: Non possono essere effettuati + di 5 prestiti contemporaneamente"
        return render_template("error/generic_error.html", error_message=error_message)

    if not student_doc:
        error_message = f"Errore: la matricola {student} non esiste nel database studenti."
        return render_template("error/generic_error.html", error_message=error_message)

    current_books = student_doc.get("isbn", [])

    # se ha più di 5 libri in prestito non può prendere altro libro
    if len(current_books) >= 5:
        error_message = f"Errore: lo studente con matricola {student} ha già troppi libri in prestito (massimo 5)."
        return render_template("error/generic_error.html", error_message=error_message)

    students_collection.update_one(
        {"Student ID": int(student)},
        {"$addToSet": {"isbn": {"$each": selection_books_isbn}}}
    )

    for isbn in selection_books_isbn:
        libro = books_collection.find_one({"isbn": isbn})
        if libro:
            # decrease of 1 copies
            print(libro["isbn"], libro["copy"]) # debug
            books_collection.update_one(
                {"isbn": isbn},
                {"$inc": {"copy": -1}}
            )
            titles.append(libro["title"])

    print(students_collection.find_one({"Student ID": int(student)}))

    return render_template('take_books.html', titles=titles, student=student)



