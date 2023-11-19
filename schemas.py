import datetime

from marshmallow import Schema, fields


# Dump only True, means it will not be expected on input body but will be sent on output response
# Load only True, means it will be expected in input but not sent as output response
# required True means will be required in input and will be returned
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    img = fields.Str(required=True)
    location = fields.Str()
    note = fields.Str()


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    img = fields.Str()
    location = fields.Str()
    note = fields.Str()

