from models.index import db, User

# GET ALL USERS
def get_all_users():
   data = User.query.all()
   data = list(map(lambda x : x.serialize(), data))
   return data

# GET ONE USER
def get_one_user(id):
    data = User.query.get(id)
    if data is None:
        return data
    return data.serialize()

# POST USER
def post_user(body):
    user = User(body["name"], body["email"], body['password'])
    db.session.add(user)
    db.session.commit()
    return user.serialize()