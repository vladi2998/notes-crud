from flask import Blueprint, request
from app.modules.notes.controllers.note_controller import NoteController
from dotenv import load_dotenv
import os

load_dotenv()

bp = Blueprint(f'routes_{os.getenv('API_VERSION')}', __name__, url_prefix=f'/api/{os.getenv('API_VERSION')}/notes')

@bp.route('', methods=['POST'])
def create_note():
    """
    Creates a new note.

    This endpoint handles POST requests to the `/notes` route. It parses the JSON request body,
    creates a new note instance, and returns the newly created note as a JSON response.

    Args:
        None

    Returns:
        JSON response:
            - `id`: Unique identifier of the created note.
            - `title`: Title of the note.
            - `content`: Content of the note.
            - `status_code`: HTTP status code (201 Created).
    """
    data = request.get_json()
    return NoteController().create_note(data)

@bp.route('', methods=['GET'])
def get_notes():
    """
    Get all notes route method
    response: [{
        'id': str,
        'title': str,
        'content': str
        'created_at': str
    }]
    """
    return NoteController().get_notes()

@bp.route('/<note_id>', methods=['GET'])
def get_note_by_id(note_id: str):
    """
    Get note by id
    props:
        note_id: str
    response: {
        'id': str,
        'title': str,
        'content': str
    }
    """
    return NoteController().get_note_by_id(note_id)

@bp.route('/<note_id>', methods=['PUT'])
def update_note(note_id: str):
    """
    Update a note route method
    props:
        note_id: str
    body: {
        'title': str (required),
        'content': str (required)
    }
    response: {
        'id': str,
        'title': str,
        'content': str
    }
    """
    data = request.get_json()
    return NoteController().update_note(note_id, data)

@bp.route('/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """
    Delete a note route method
    props:
        note_id: str
    response: json message
    """
    return NoteController().delete_note(note_id)
