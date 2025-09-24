from flask import Blueprint, render_template

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    # Define buttons as a list of dictionaries
    buttons_libri = [
        {"label": "Inserisci Nuovo Libro", "action": "/insert_books", "method": "get", "bg_color": "purple", "icon_class1": "fas fa-plus fa-xs", "icon_class2": "fas fa-book fa-fw mr-2"},
        {"label": "Vai alla Lista Libri", "action": "/list", "method": "get", "bg_color": "blue", "icon_class1": "fas fa-list fa-fw mr-2"},
        {"label": "Libri Disponibili al Prestito", "action": "/available_books", "method": "get", "bg_color": "teal", "icon_class1": "fas fa-book-open fa-fw mr-2"},
        {"label": "Libri Presi in Prestito", "action": "/borrowed_books", "method": "get", "bg_color": "indigo", "icon_class1": "fas fa-hand-holding fa-fw mr-2"},
        {"label": "Elimina un Libro", "action": "/delete_books", "method": "get", "bg_color": "red", "icon_class1": "fas fa-trash fa-fw mr-2"}
    ]

    buttons_prestiti = [
        {"label": "Prendi un Libro in Prestito", "action": "/borrow_books", "method": "get", "bg_color": "yellow", "icon_class1": "fas fa-right-left fa-fw mr-2"},
        {"label": "Restituzione Libro", "action": "/return_books", "method": "get", "bg_color": "green", "icon_class1": "fas fa-right-left fa-fw mr-2"}
    ]

    buttons_studenti = [
        {"label": "Inserisci un Nuovo Studente", "action": "/insert_students", "method": "get", "bg_color": "green", "icon_class1": "fas fa-plus fa-xs", "icon_class2": "fas fa-user fa-fw mr-2"}
    ]

    pagetitle = "Student's Library Home"
    return render_template('new/home.html', pagetitle=pagetitle, btn_libri=buttons_libri, btn_prestiti=buttons_prestiti, btn_studenti=buttons_studenti)
