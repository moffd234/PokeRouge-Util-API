import logging

from flask import Blueprint, jsonify, Response

from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils

weaknesses_bp: Blueprint = Blueprint("weaknesses_bp", __name__)
type_util: TypeUtils = TypeUtils()
api_logger = logging.getLogger("api")


def return_output(output: dict | list) -> tuple[Response, int] | Response:
    if "error" in output:
        api_logger.error(f"API call returned an error: {output.get('error')}")
        return jsonify(output), 400

    return jsonify(output)


def call_and_catch(func: callable, *args) -> tuple[Response, int] | Response:
    try:
        output: list = func(*args)
        return return_output(output)

    except ValueError as error:
        api_logger.warning(f"Invalid input provided to API: {error}", exc_info=True)
        return jsonify({"error": str(error)}), 404


@weaknesses_bp.route('/weaknesses/summary/<string:pokemon_species>', methods=['GET'])
def get_weakness_summary(pokemon_species: str) -> tuple[Response, int] | Response:
    api_logger.info(f"Received request for weakness summary for: {pokemon_species}")
    pokemon: Pokemon | None = Pokemon.query.filter_by(name=pokemon_species.upper()).first()

    if not pokemon:
        api_logger.warning(f"Pokemon '{pokemon_species}' not found for weakness summary.")
        return jsonify({'message': 'Pokemon not found'}), 404

    output: dict = type_util.get_weakness_summary(pokemon)
    return return_output(output)


@weaknesses_bp.route('/weaknesses/offensive/<string:pokemon_type>', methods=['GET'])
def get_offensive_weaknesses(pokemon_type: str) -> tuple[Response, int] | Response:
    api_logger.info(f"Received request for offensive weaknesses for: {pokemon_type}")
    return call_and_catch(type_util.get_offensive_weaknesses, pokemon_type)


@weaknesses_bp.route('/weaknesses/defensive/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('/weaknesses/defensive/<string:type_1>/<string:type_2>', methods=['GET'])
def get_defensive_weaknesses(type_1: str, type_2: str = None) -> tuple[Response, int] | Response:
    api_logger.info(f"Received request for defensive weaknesses for: {type_1}, {type_2}")
    return call_and_catch(type_util.get_defensive_weaknesses, type_1, type_2)


@weaknesses_bp.route('/weaknesses/immunities/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('/weaknesses/immunities/<string:type_1>/<string:type_2>', methods=['GET'])
def get_immunities(type_1: str, type_2: str = None) -> tuple[Response, int] | Response:
    api_logger.info(f"Received request for immunities for: {type_1}, {type_2}")
    return call_and_catch(type_util.get_immunities, type_1, type_2)


@weaknesses_bp.route('/weaknesses/immune-defenders/<string:type_1>', methods=['GET'])
def get_immune_defenders(type_1: str) -> tuple[Response, int] | Response:
    api_logger.info(f"Received request for immune defenders for attacker type: {type_1}")
    return call_and_catch(type_util.get_immune_defenders, type_1)
