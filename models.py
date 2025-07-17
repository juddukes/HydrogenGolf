from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PromptCache(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, unique=True, nullable=False)
    response = db.Column(db.Text, nullable=False)
