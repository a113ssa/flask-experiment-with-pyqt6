from db import db


class StoryModel(db.Model):
  __tablename__ = 'stories'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(255), unique=False, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship('UserModel', back_populates='stories')
