from marshmallow import Schema, fields, ValidationError

def not_empty_string(value: str):
    if not value.strip():
        raise ValidationError("Field cannot be empty")

class CreateNoteSchema(Schema):
    title = fields.Str(
        required=True,
        validate=not_empty_string,
        error_messages={"required": "title can't be empty"}
    )
    content = fields.Str(
        required=True,
        validate=not_empty_string,
        error_messages={"required": "content can't be empty"}
    )

class ResponseNoteSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    content = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class UpdateNoteSchema(Schema):
    title = fields.Str(
        validate=not_empty_string,
        error_messages={"required": "title can't be empty"}
    )
    content = fields.Str(
        validate=not_empty_string,
        error_messages={"required": "content can't be empty"}
    )
