from api.core import Mixin
from .base import db


class Entitlement(Mixin, db.Model):
    """Entitlement Table."""

    __tablename__ = "entitlement"

    name = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, unique=True, primary_key=True)
    bsg_handle = db.Column(db.String, nullable=False)
    source_id = db.Column(db.String, nullable=False)
    call_letters = db.Column(db.String, nullable=False)
    billing_load_date = db.Column(db.String, nullable=False)
    controller_load_date = db.Column(db.String, nullable=False)

    def __init__(self, name: str, id: int, bsg_handle: str, source_id: str, call_letters: str, billing_load_date: str, controller_load_date: bool):
        self.name = name
        self.id = id
        self.bsg_handle = bsg_handle
        self.source_id = source_id
        self.call_letters = call_letters
        self.billing_load_date = billing_load_date
        self.controller_load_date = controller_load_date


        
    def __repr__(self):
        return f"<Entitlement {self.name, self.id, self.bsg_handle, self.source_id, self.call_letters, self.billing_load_date, self.controller_load_date}>"

