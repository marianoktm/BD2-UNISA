from flask import Blueprint, render_template, request
from config.config import get_databases
from datetime import datetime
import random



booksBlueprint = Blueprint("books", __name__)

get_databases = get_databases()
books = get_databases["books"]

@booksBlueprint.post("/insert_books")
def insert_books():
    return render_template("insert_books.html")

@booksBlueprint.post("/add_books")
def add_books():

    title = request.form.get("title")
    isbn = request.form.get("isbn")
    pageCount = int(request.form.get("pageCount"))

    publishedDate_raw = request.form.get("publishedDate")
    publishedDate = datetime.fromisoformat(publishedDate_raw)  # datetime con timezone

    authors_raw = request.form.get("authors", "")
    categories_raw = request.form.get("categories", "")

    authors = [a.strip() for a in authors_raw.splitlines() if a.strip()]
    categories = [c.strip() for c in categories_raw.splitlines() if c.strip()]
    copy = int(request.form.get("copy"))

    #book_id random not present in the database
    def generate_unique_book_id():
        while True:
            book_id = random.randint(1, 1000)  # range a piacere
            exists = books.find_one({"book_id": book_id})
            if not exists:
                return book_id


    new_book = {
        "title": title,
        "isbn": isbn,
        "pageCount": pageCount,
        "publishedDate": publishedDate,
        "authors": authors,
        "categories": categories,
        "book_id" : generate_unique_book_id(),
        "copy": copy

    }

    existing_book = books.find_one({"isbn": new_book["isbn"]})

    if existing_book:
        error_message = f"Errore: Un libro con ISBN '{isbn}' esiste già."
        return render_template("error/error_insert_book.html", error_message=error_message)

    books.insert_one(new_book)

    return render_template("add_books.html", new_book=new_book)


