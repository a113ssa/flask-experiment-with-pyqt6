from marshmallow import Schema, fields
from marshmallow.validate import OneOf

ALLOWED_MOODS = ['neutral', 'curious', 'fear', 'happy']

class GameResponseSchema(Schema):
    questText = fields.Str(dump_only=True)
    responseVariants = fields.List(fields.Str(), dump_only=True)
    mood = fields.Str(dump_only=True, validate=OneOf(ALLOWED_MOODS))


class GameRequestSchema(Schema):
    message = fields.Str(required=True)


class UserResponseSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    nickname = fields.Str(required=True, dump_only=True)
    health = fields.Int(required=True, dump_only=True)


class UserRequestSchema(Schema):
    nickname = fields.Str(required=True)

class UserUpdateRequestSchema(Schema):
    health = fields.Int(required=True)
