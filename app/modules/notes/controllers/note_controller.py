from app.modules.notes.models.note import Note, notes
from app.modules.notes.schemas.note_schema import NoteSchema
from flask import jsonify
from marshmallow import ValidationError

from app.modules.notes.services.notes_service import NoteService

class NoteController:
  def __init__(self):
    self.schema = NoteSchema()

  def create_note(self, data):
    try:
        validated_data = self.schema.load(data)
    except ValidationError as err:
        return {'error': err.messages}, 400

    note = NoteService.create_note(validated_data)

    response_data = {
      "id": note.id,
      "title": note.title,
      "content": note.content
    }

    return jsonify(response_data), 201
