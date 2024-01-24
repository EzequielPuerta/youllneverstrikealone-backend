from mongoengine import Document, fields


# https://plus.codes/map
class Gatherings(Document):
    ig_name = fields.StringField(required=True, null=False)
    ig_link = fields.StringField(required=True, null=False)
    plus_code = fields.StringField(required=True, null=False)
