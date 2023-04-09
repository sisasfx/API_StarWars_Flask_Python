from models.index import db, Planets

# GET ALL PLANETS
def get_all_planets():
    data = Planets.query.all()
    data = list(map(lambda x : x.serialize(), data))
    return data

# GET ONE PLANET
def get_one_planet(id):
    data = Planets.query.get(id)
    if data is None:
        return data
    return data.serialize()

# POST PLANET
def post_planet(body):
    planet = Planets(body['name'], body['description'])
    db.session.add(planet)
    db.session.commit()
    return planet.serialize()