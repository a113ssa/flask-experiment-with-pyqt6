from db import db


class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  nickname = db.Column(db.String(80), unique=True, nullable=False)
  health = db.Column(db.Integer, unique=False, nullable=False)
  stories = db.relationship('StoryModel', back_populates='user', lazy='dynamic', cascade='all, delete')

  def __repr__(self):
    return f'<User id={self.id} nickname={self.nickname} health={self.health}>'
