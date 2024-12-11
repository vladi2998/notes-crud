from app.modules.notes.models.note import Note
from app import db
import datetime as dt

class NoteService:
    @staticmethod
    def create_note(data):
        """
        Create a new note in the database.

        Args:
            data (dict): A dictionary containing 'title' and 'content'.

        Returns:
            Note: The created Note object.
        """
        note = Note(
            title=data['title'],
            content=data['content']
        )
        db.session.add(note)
        db.session.commit()
        return note

    @staticmethod
    def get_note_by_id(note_id: str):
        """
        Get a note based on the note id.

        Args:
            note_id (str): The ID of the note to retrieve.

        Returns:
            Note: The Note object if found and not deleted, otherwise None.
        """
        note = Note.query.get(note_id)
        if note is None or note.deleted_at is not None:
            return None
        return note


    @staticmethod
    def get_notes():
        """
        Get all notes that are not deleted.

        Returns:
            list: A list of Note objects.
        """
        return Note.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_note(note_id: str, data):
        """
        Update an existing note in the database.

        Args:
            note_id (str): The ID of the note to update.
            data (dict): A dictionary containing 'title' and/or 'content'.

        Returns:
            Note: The updated Note object, or None if not found.
        """
        note = Note.query.get(note_id)
        if note is None or note.deleted_at is not None:
            return None

        note.updated_at = dt.datetime.utcnow()
        if 'title' in data:
            note.title = data['title']
        if 'content' in data:
            note.content = data['content']

        db.session.commit()
        return note

    @staticmethod
    def delete_note(note_id: str):
        """
        Delete an note in the database if the deleted_at == None.

        Args:
            note_id (str): The ID of the note to update.

        Returns:
            Note: The updated Note object, or None if not found.
        """
        note = Note.query.get(note_id)
        if note is None or note.deleted_at is not None:
            return None

        note.deleted_at = dt.datetime.utcnow()

        db.session.commit()
        return note
