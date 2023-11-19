import datetime

from marshmallow import Schema, fields


# Dump only True, means it will not be expected on input body but will be sent on output response
# Load only True, means it will be expected in input but not sent as output response
# required True means will be required in input and will be returned
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    img = fields.Str(required=True)
    note = fields.Str()


class PlainLocationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    organization_id = fields.Str(required=True)


class LocationSchema(PlainLocationSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemSchema(PlainItemSchema):
    location_id = fields.Str(required=True, load_only=True)
    location = fields.Nested(PlainLocationSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    img = fields.Str()
    note = fields.Str()
    location_id = fields.Str()

