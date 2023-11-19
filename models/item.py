from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    img = db.Column(db.String(250), unique=False, nullable=False)
    note = db.Column(db.String(250), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), unique=False, nullable=False)
    location = db.relationship("LocationModel", back_populates="items")
