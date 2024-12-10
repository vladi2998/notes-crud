from flask import Blueprint, request, jsonify
from app.models import Note, notes

bp = Blueprint('routes', __name__)

@bp.route('/notes', methods=['POST'])
def create_note():
    """
    Create a new note route method
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

    if not title or not content:
        return jsonify({'error': 'Invalid body structure'}), 400

    note = Note(
        title=data['title'],
        content=data['content']
    )
    notes.append(note)

    return jsonify(
        {
            'id': note.id,
            'title': note.title,
            'content': note.content
        }
    ), 201

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
