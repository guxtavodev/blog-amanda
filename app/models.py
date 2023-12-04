from app import db, app
from datetime import datetime

class Post(db.Model):
  __tablename__ = "post"
  title = db.Column(db.String(80), nullable=False)
  body = db.Column(db.Text, nullable=False)
  body_markdown = db.Column(db.Text, nullable=False) # Texto em markdown, antes de converter para o body como HTML
  pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  img = db.Column(db.String())
  id = db.Column(db.String(), primary_key=True)
  endpoint = db.Column(db.String())

  def __init__(self, title, body, body_markdown, img, id, endpoint):
    self.title = title
    self.body = body
    self.body_markdown = body_markdown
    self.img = img
    self.id = id
    self.endpoint = endpoint

class Comentarios(db.Model):
  __tablename__ = "comentarios"
  autor = db.Column(db.String())
  text = db.Column(db.String())
  id = db.Column(db.String(), primary_key=True)
  post = db.Column(db.String())

  def __init__(self, autor, text, id, post):
    self.autor = autor
    self.text = text
    self.id = id
    self.post = post

with app.app_context():
  db.create_all()