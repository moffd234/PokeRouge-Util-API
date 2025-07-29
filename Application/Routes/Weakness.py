from flask import Blueprint, jsonify

from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils

weaknesses_bp: Blueprint = Blueprint("weaknesses_bp", __name__)
type_util: TypeUtils = TypeUtils()

@weaknesses_bp.route('/weaknesses/<string:pokemon_species>', methods=['GET'])
def get_weakness_summary(pokemon_species: str):
    pokemon: Pokemon | None = Pokemon.query.filter_by(name=pokemon_species.upper()).first()

    if not pokemon:
        return jsonify({'message': 'Pokemon not found'}), 404

    output: dict = type_util.get_weakness_summary(pokemon)

    if "error" in output:
        return jsonify(output), 400

    return jsonify(output)
