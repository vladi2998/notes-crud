from app.modules.notes.models.note import Note
from app import db

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
