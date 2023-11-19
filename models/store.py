from db import db

'''
    lazy = "dynamic" means items column will be queried and prepopulated only on request and not always
    cascade means if store is deleted, all its items will be deleted as well.
'''


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
