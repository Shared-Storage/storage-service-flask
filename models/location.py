from db import db

'''
    lazy = "dynamic" means items column will be queried and prepopulated only on request and not always
    cascade means if location is deleted, all its items will be deleted as well.
'''


class LocationModel(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="location", lazy="dynamic")
