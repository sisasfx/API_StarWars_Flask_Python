from models.index import db, User, Planets, Characters

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_personajes = db.Column(db.Integer, db.ForeignKey('characters.id'))
    user = db.relationship(User)
    planets = db.relationship(Planets)
    characters = db.relationship(Characters)

    def __init__(self, user, planets, characters):
        self.user = user
        self.planets = planets
        self.characters  = characters

    def serialize(self):
        return {
            "id" : self.id,
            "usuario" : self.id_usuario,
            "planeta" : self.id_planets
        }