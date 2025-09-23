from flask import Blueprint, render_template, request
from db.DatabaseSingleton import get_databases

delete_booksBlueprint = Blueprint('delete_books', __name__)

database = get_databases()
books = database['books']


@delete_booksBlueprint.get('/delete_books')
def delete_books():
    return render_template("delete_books.html")


@delete_booksBlueprint.post('/trash_books')
def trash_books():

    title = request.form.get('title')
    isbn = request.form.get('isbn')

    existing_book = books.find_one({"isbn": isbn})
    if not existing_book:
        error_message = f"Errore: Nessun libro trovato con ISBN '{isbn}'."
        return render_template("error/error_delete_book.html", error_message=error_message)
    trash_book = {
        'title': title,
        'isbn': isbn
    }

    books.delete_one({"isbn": isbn})
    return render_template("trash_books.html", trash_book=trash_book)