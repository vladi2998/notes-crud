import datetime as dt
import uuid

class Note:
    def __init__(self, title: str, content: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Note(name={self.title!r})>'.format(self=self)

notes = []
