from marshmallow import Schema, fields, ValidationError

def not_empty_string(value: str):
    if not value.strip():
        raise ValidationError("Field cannot be empty")

class NoteSchema(Schema):
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
