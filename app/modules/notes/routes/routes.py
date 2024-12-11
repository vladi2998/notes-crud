from flask import Blueprint, request, jsonify
from app.modules.notes.controllers.note_controller import NoteController
from app import db
from sqlalchemy.sql import text

bp = Blueprint('routes', __name__)

@bp.route('/notes', methods=['POST'])
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
    controller = NoteController()  # Inject db_session
    return controller.create_note(data)

@bp.route('/db-check', methods=['GET'])
def check_db_connection():
    """
    Verifies the database connection.

    This endpoint handles GET requests to the `/db-check` route. It performs a basic query
    to ensure that the database connection is active and returns a response indicating
    the status of the connection.

    Args:
        None

    Returns:
        JSON response:
            - `message`: A string indicating whether the connection is successful or failed.
            - `status_code`: HTTP status code (200 OK or 500 Internal Server Error).
    """
    try:
        # Realiza una consulta básica para verificar la conexión
        result = db.session.execute(text('SELECT 1')).scalar()
        if result == 1:
            return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        return jsonify({"message": f"Database connection failed: {str(e)}"}), 500


@bp.route('/notes', methods=['GET'])
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
    global notes

    return jsonify([
        {
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at
        } for note in notes]), 200

@bp.route('/notes/<note_id>', methods=['PUT'])
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
    title = data.get('title', None)
    content = data.get('content', None)

    if not title and not content:
        return jsonify({'error': 'Invalid body structure'}), 400

    note = next((note for note in notes if note.id == note_id), None)
    if note is None:
        return jsonify({'error': 'Note not found'}), 404

    note.title = title if title else note.title
    note.content = content if content else note.content

    return jsonify(
        {
            'id': note.id,
            'title': note.title,
            'content': note.content
        }
    ), 200

@bp.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """
    Delete a note route method
    props:
        note_id: str
    response: None
    """
    global notes

    note = next((note for note in notes if note.id == note_id), None)
    if note is None:
        return jsonify({'error': 'Note not found'}), 404

    notes = [note for note in notes if note.id != note_id]

    return f'Note with id: {note_id} was deleted', 200
