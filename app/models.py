from . import db

class Article(db.Model):
    __tablename__ = 'articles'
    pmid = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.Unicode)
    body = db.Column(db.UnicodeText)
