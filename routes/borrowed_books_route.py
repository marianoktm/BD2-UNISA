from flask import Blueprint, render_template

borrowedBlueprint = Blueprint("borrowedBooks", __name__)


@borrowedBlueprint.get("/borrowed_books")
def borrowed_books():
    return render_template('borrowed_books.html')
