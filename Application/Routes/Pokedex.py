from flask import Blueprint, jsonify, Response
from Application.Models.Pokemon import Pokemon

pokedex_bp: Blueprint = Blueprint('pokedex_bp', __name__)

@pokedex_bp.route('/pokedex/<string:species>', methods=['GET'])
def get_species_entry(species: str) -> tuple[Response, int] | Response:
    pokemon: Pokemon = Pokemon.query.filter_by(name=species.upper()).first()

    if not pokemon:
        return jsonify({'message': 'Pokemon not found'}), 404

    return jsonify(pokemon.to_dict())