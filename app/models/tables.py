from app import db


class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True)
  passaword = db.Column(db.String)
  name = db.Column(db.String)
  email = db.Column(db.String, unique=True)

  def __inti__(self, username, passaword, name, email):
    self.username = username
    self.passaword = passaword
    self.name = name
    self.email = email

  def __repr__(self):
    return "<User %r>" % self.username