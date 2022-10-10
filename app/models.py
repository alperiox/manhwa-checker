from app import db

class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    status = db.Column(db.String(64)) 
    slug = db.Column(db.String(128), unique=True)
    last_updated = db.Column(db.DateTime)
    url = db.Column(db.String(255))
    latest_chapter = db.Column(db.Integer)
    read = db.Column(db.Boolean, default=False)
    platform = db.Column(db.String(64))

    def __repr__(self):
        return f"Comic <{self.slug} | {self.platform}>"
