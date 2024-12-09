from marshmallow import Schema, fields
from marshmallow.validate import OneOf

ALLOWED_MOODS = ['neutral', 'curious', 'fear', 'happy']

class GameResponseSchema(Schema):
    questText = fields.Str(dump_only=True)
    responseVariants = fields.List(fields.Str(), dump_only=True)
    mood = fields.Str(dump_only=True, validate=OneOf(ALLOWED_MOODS))


class GameRequestSchema(Schema):
    message = fields.Str(required=True)
