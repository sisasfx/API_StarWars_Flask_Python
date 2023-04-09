from models.index import db, Characters

# GET ALL CHARACTERS
def get_all_characters():
    data = Characters.query.all()
    data = list(map(lambda x : x.serialize(), data))
    return data

# GET ONE CHARACTER
def get_one_character(id):
    data = Characters.query.get(id)
    if data is None:
        return data
    return data.serialize()

# POST CHARACTER
def post_character(body):
    character = Characters(body['name'], body['description'])
    db.session.add(character)
    db.session.commit()
    return character.serialize()