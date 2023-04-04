from models.index import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "description" : self.description
        }
