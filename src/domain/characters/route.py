from flask import request
from models.index import Characters
import domain.characters.controller as Controller

def character_router(app):
    # GET ALL CHARACTERS
    @app.route('/people', methods=['GET'])
    def get_all_characters():
        return Controller.get_all_characters()

    @app.route('/people/<int:id>', methods=['GET'])
    def get_one_character(id):
        return Controller.get_one_character(id)
    
    @app.route('/people', methods=['POST'])
    def post_character():
        body = request.get_json()
        return Controller.post_character(body)