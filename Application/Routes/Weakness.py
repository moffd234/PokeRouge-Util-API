from flask import Blueprint, jsonify, Response

from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils

weaknesses_bp: Blueprint = Blueprint("weaknesses_bp", __name__)
type_util: TypeUtils = TypeUtils()


def return_output(output: dict | list) -> tuple[Response, int] | Response:
    if "error" in output:
        return jsonify(output), 400

    return jsonify(output)


@weaknesses_bp.route('/weaknesses/summary/<string:pokemon_species>', methods=['GET'])
def get_weakness_summary(pokemon_species: str):
    pokemon: Pokemon | None = Pokemon.query.filter_by(name=pokemon_species.upper()).first()

    if not pokemon:
        return jsonify({'message': 'Pokemon not found'}), 404

    output: dict = type_util.get_weakness_summary(pokemon)
    return return_output(output)


@weaknesses_bp.route('weaknesses/offensive/<string:pokemon_type>', methods=['GET'])
def get_offensive_weaknesses(pokemon_type: str):
    output: list = type_util.get_offensive_weaknesses(pokemon_type)

    return return_output(output)
