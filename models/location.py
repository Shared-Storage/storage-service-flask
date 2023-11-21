from db import db

'''
    lazy = "dynamic" means items column will be queried and prepopulated only on request and not always
    cascade means if location is deleted, all its items will be deleted as well.
'''


class LocationModel(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    organization_id = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(200), nullable=True)
    items = db.relationship("ItemModel", back_populates="location", lazy="dynamic")
