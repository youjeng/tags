from config import db

class Tag(db.Model):
    __fillable__ = [ 'name' ]

    def __repr__(self):
        return '<Tag %r>' % self.name
