from flask import Blueprint, render_template

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    # Define buttons as a list of dictionaries
    buttons_libri = [
        {"label": "Inserisci Nuovo Libro", "action": "/insert_books", "method": "get"},
        {"label": "Vai alla Lista Libri", "action": "/list", "method": "get"},
        {"label": "Libri Disponibili al Prestito", "action": "/available_books", "method": "get"},
        {"label": "Libri Presi in Prestito", "action": "/borrowed_books", "method": "get"},
        {"label": "Elimina un Libro", "action": "/delete_books", "method": "get"}
    ]

    buttons_prestiti = [
        {"label": "Prendi un Libro in Prestito", "action": "/borrow_books", "method": "get"}
    ]

    buttons_studenti = [
        {"label": "Inserisci un Nuovo Studente", "action": "/insert_students", "method": "get"}
    ]

    return render_template('new/home.html', btn_libri=buttons_libri, btn_prestiti=buttons_prestiti, btn_studenti=buttons_studenti)
