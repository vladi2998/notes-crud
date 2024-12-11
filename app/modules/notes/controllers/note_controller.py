from app.modules.notes.schemas.note_schema import CreateNoteSchema, ResponseNoteSchema, UpdateNoteSchema
from flask import jsonify
from marshmallow import ValidationError

from app.modules.notes.services.notes_service import NoteService

class NoteController:
    def __init__(self):
        self.create_schema = CreateNoteSchema()
        self.response_schema = ResponseNoteSchema()
        self.update_schema = UpdateNoteSchema()

    def create_note(self, data: dict):
        try:
            validated_data = self.create_schema.load(data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        note = NoteService.create_note(validated_data)

        response_data = {
            "id": note.id,
            "title": note.title,
            "content": note.content
        }

        return jsonify(response_data), 201

    def get_note_by_id(self, note_id: str):
        note = NoteService.get_note_by_id(note_id)
        if note is None:
            return {'error': 'Note not found or already deleted'}, 404

        response_data = self.response_schema.dump(note)

        return jsonify(response_data), 200

    def get_notes(self):
        notes = NoteService.get_notes()
        serialized_notes = self.response_schema.dump(notes, many=True)
        return jsonify(serialized_notes), 200

    def update_note(self, note_id: str, data: dict):
        try:
            validated_data = self.update_schema.load(data, partial=True)
        except ValidationError as err:
            return {'error': err.messages}, 400

        note = NoteService.update_note(note_id, validated_data)

        if note is None:
            return {'error': 'Note not found or already deleted'}, 404

        response_data = self.response_schema.dump(note)

        return jsonify(response_data), 200

    def delete_note(self, note_id: str):
        note = NoteService.delete_note(note_id)

        if note is None:
            return {'error': 'Note not found or already deleted'}, 404

        return {'message': f'Note with id: {note_id} was deleted successfully'}, 200
