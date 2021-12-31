from api.core import Mixin
from .base import db


class Status(Mixin, db.Model):
    """Status Table."""

    __tablename__ = "status"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    load_start = db.Column(db.String, nullable=False)
    load_completed = db.Column(db.String, nullable=False)
    merlin_ready = db.Column(db.String, nullable=False)
    file = db.Column(db.String, nullable=False)

    def __init__(self, name: str, id: int, type: str, load_start: str, load_completed: str, merlin_ready: str, file: str  ):
        self.name = name
        self.id = id
        self.type = type
        self.load_start = load_start
        self.load_completed = load_completed
        self.merlin_ready = merlin_ready
        self.file = file
        
    def __repr__(self):
        return f"<Status {self.name, self.id, self.type, self.load_start, self.load_completed, self.merlin_ready, self.file}>"

