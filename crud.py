"""CRUD Operations: Functions to create, retrieve, update, or delete data from the database."""

from model import db, User, Cafe, Bookmark, Note, connect_to_db
from flask import flash


### FUNCTIONS TO CREATE ####


def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    return user


def create_cafe(id, name, address, city, state, phone, latitude, longitude, img_url):
    """Create and return a cafe."""

    cafe = Cafe(cafe_id=id, name=name, address=address, city=city , state=state, phone=phone, latitude=latitude, longitude=longitude, img_url=img_url)

    return cafe


def create_bookmark(user, cafe): 
    """Create and return a bookmark."""

    bookmark = Bookmark(user_id=user, cafe_id=cafe)

    return bookmark


def create_note(user, bookmark, note):
    """Create and return a note for a bookmark."""

    note = Note(user_id=user, bookmark_id=bookmark, note=note)

    return note


### FUNCTIONS TO RETRIEVE ###


def get_user_by_id(user_id):
    """Return a user by user id."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user with a given email."""

    return User.query.filter(User.email == email).first()


def get_cafe_by_id(cafe_id):
    """Return a cafe by cafe id."""

    return Cafe.query.get(cafe_id)


def get_cafe_by_bookmark_id(bookmark_id):
    """Return a cafe by bookmark id."""

    bookmark = Bookmark.query.filter(Bookmark.bookmark_id == bookmark_id).first()

    return bookmark.cafe


def get_all_user_bookmarks(user_id):
    """Return all bookmarks for a user by user id."""

    return Bookmark.query.filter(Bookmark.user_id == user_id).all()


def get_bookmark_by_user_and_cafe_id(user_id, cafe_id):
    """Return a bookmark for a user by user and cafe id."""

    return Bookmark.query.filter(Bookmark.user_id == user_id, Bookmark.cafe_id == cafe_id).first()


def get_note_by_bookmark_id(bookmark_id):
    """Return a note by bookmark id."""

    return Note.query.filter(Note.bookmark_id == bookmark_id).first()


### FUNCTIONS TO UPDATE ###


def update_note(existing_note, new_note):
    """Update an existing note."""

    try:
        existing_note.note = new_note
        db.session.add(existing_note)
        db.session.commit()
    except Exception as e:
        flash("Sorry, we couldn't update your note.")
        print(e)


### FUNCTIONS TO DELETE ###


def delete_note(existing_note):
    """Delete an existing note."""

    db.session.delete(existing_note)
    db.session.commit()


if __name__ == "__main__":
    from app import app
    connect_to_db(app)