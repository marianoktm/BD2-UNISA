from flask import Blueprint, render_template
from db.DatabaseSingleton import get_databases

borrowedBlueprint = Blueprint("borrowedBooks", __name__)

databases = get_databases()
books_collection = databases["books"]


@borrowedBlueprint.get("/borrowed_books")
def borrowed_books():

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
            "$match": {
                "borrowed_by.0": {"$exists": True}  # only books to borrow
            }
        }
    ]

    books = list(books_collection.aggregate(pipeline))
    return render_template("borrowed_books.html", books=books)

