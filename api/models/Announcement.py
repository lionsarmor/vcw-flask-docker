from api.core import Mixin
from .base import db


class Announcement(Mixin, db.Model):
    """Announcement Table."""

    __tablename__ = "announcement"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time_of_creation = db.Column(db.String, nullable=False)
    poster = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name: str, id: int, time_of_creation: str, poster: str, subject: str, description: str ):
        self.name = name
        self.id = id
        self.time_of_creation = time_of_creation
        self.poster = poster
        self.subject = subject
        self.description = description
        
    def __repr__(self):
        return f"<Announcement {self.name, self.id, self.time_of_creation, self.poster, self.subject, self.description}>"
