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


@weaknesses_bp.route('weaknesses/defensive/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('weaknesses/defensive/<string:type_1>/<string:type_2>', methods=['GET'])
def get_defensive_weaknesses(type_1: str, type_2: str = None):
    output: list = type_util.get_defensive_weaknesses(type_1, type_2)

    return_output(output)

@weaknesses_bp.route('weaknesses/immunities/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('weaknesses/immunities/<string:type_1>/<string:type_2>', methods=['GET'])
def get_immunities(type_1: str, type_2: str = None):
    output: list = type_util.get_immunities(type_1, type_2)

    return_output(output)