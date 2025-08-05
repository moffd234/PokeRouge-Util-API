import logging

from flask import Blueprint, jsonify, Response
from Application.Models.Pokemon import Pokemon

pokedex_bp: Blueprint = Blueprint('pokedex_bp', __name__)
pokedex_logger = logging.getLogger("api")

@pokedex_bp.route('/pokedex/<string:species>', methods=['GET'])
def get_species_entry(species: str) -> tuple[Response, int] | Response:
    pokedex_logger.info(f"Received Pokedex request for: {species}")
    pokemon: Pokemon = Pokemon.query.filter_by(name=species.upper()).first()

    if not pokemon:
        pokedex_logger.warning(f"Pokedex entry not found for: {species}")
        return jsonify({'message': 'Pokemon not found'}), 404

    pokedex_logger.info(f"Successfully retrieved Pokedex entry for species: {species}")
    return jsonify(pokemon.to_dict())