from api.core import Mixin
from .base import db


class Channel(Mixin, db.Model):
    """Channel Table."""

    __tablename__ = "channel"

    name = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, unique=True, primary_key=True)
    channel_number = db.Column(db.String, nullable=False)
    call_sign = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    source_id = db.Column(db.String, nullable=False)
    hdtv = db.Column(db.String, nullable=False)
    load_date = db.Column(db.String, nullable=False)

    def __init__(self, name: str, id: int, channel_number: str, call_sign: str, full_name: str, source_id: str, hgtv: bool, load_date: str  ):
        self.name = name
        self.id = id
        self.channel_number = channel_number
        self.call_sign = call_sign
        self.full_name = full_name
        self.source_id = source_id
        self.hgtv = hgtv
        self.load_date = load_date
        
    def __repr__(self):
        return f"<Channel {self.name, self.id, self.channel_number, self.call_sign, self.full_name, self.source_id, self.hgtv, self.load_date}>"

