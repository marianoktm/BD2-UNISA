from flask import Blueprint, render_template

borrowBlueprint = Blueprint("borrowBooks", __name__)


@borrowBlueprint.get("/borrow_books")
def borrow_books():
    return render_template('borrow_books.html')
