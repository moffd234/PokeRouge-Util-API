import logging

from flask import Blueprint, jsonify, Response
from Application.Utils.TypeUtils import get_offensive_weaknesses, get_defensive_strengths, \
    get_weakness_strength_summary, get_immunities, get_immune_defenders, get_defensive_weaknesses, \
    get_offensive_strengths
from Application.Models.Pokemon import Pokemon

weaknesses_bp: Blueprint = Blueprint("weaknesses_bp", __name__)
api_logger = logging.getLogger("api")


def return_output(output: dict | list) -> tuple[Response, int] | Response:
    """
    Returns a Flask JSON response based on the provided output.

    If the output contains an "error" key, a 400 Bad Request response is returned.
    Otherwise, the data is returned as a standard JSON response.

    :param output: The output data to return, either a dictionary or list.
    :return: A Flask JSON response, optionally with a status code.
    """
    if "error" in output:
        api_logger.error(f"API call returned an error: {output.get('error')}")
        return jsonify(output), 400

    return jsonify(output)


def call_and_catch(func, *args) -> tuple[Response, int] | Response:
    """
    Executes a given function and returns its output as a JSON response.

    Wraps the function call in a try/except block to handle ValueError exceptions.
    If a ValueError occurs, returns a 404 response with the error message.

    :param func: The function to execute.
    :param args: Positional arguments to pass to the function.
    :return: A Flask JSON response containing the function output or an error.
    """
    try:
        output: list = func(*args)
        return return_output(output)

    except ValueError as error:
        api_logger.warning(f"Invalid input provided to API: {error}", exc_info=True)
        return jsonify({"error": str(error)}), 404


@weaknesses_bp.route('/weaknesses/summary/<string:pokemon_species>', methods=['GET'])
def bp_get_weakness_summary(pokemon_species: str) -> tuple[Response, int] | Response:
    """
    Retrieves a pokémon's type weakness and strength summary.

    :param pokemon_species: The name of the pokémon to query.
    :return: JSON response containing the weakness/strength summary, or 404 if not found.
    """
    api_logger.info(f"Received request for weakness summary for: {pokemon_species}")
    pokemon: Pokemon | None = Pokemon.query.filter_by(name=pokemon_species.upper()).first()

    if not pokemon:
        api_logger.warning(f"pokemon '{pokemon_species}' not found for weakness summary.")
        return jsonify({'message': 'Pokemon not found'}), 404

    output: dict = get_weakness_strength_summary(pokemon)
    return return_output(output)


@weaknesses_bp.route('/weaknesses/offensive/<string:pokemon_type>', methods=['GET'])
def bp_get_offensive_weaknesses(pokemon_type: str) -> tuple[Response, int] | Response:
    """
    Retrieves all pokémon types that take less damage from the given attacking type.

    :param pokemon_type: The attacking pokémon type to evaluate.
    :return: JSON response containing offensive weaknesses.
    """

    api_logger.info(f"Received request for offensive weaknesses for: {pokemon_type}")
    return call_and_catch(get_offensive_weaknesses, pokemon_type)


@weaknesses_bp.route('/weaknesses/defensive/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('/weaknesses/defensive/<string:type_1>/<string:type_2>', methods=['GET'])
def bp_get_defensive_weaknesses(type_1: str, type_2: str = None) -> tuple[Response, int] | Response:
    """
    Retrieves all pokémon types that deal more damage to the given defensive types.

    :param type_1: The primary defensive pokémon type.
    :param type_2: The secondary defensive pokémon type, if applicable.
    :return: JSON response containing defensive weaknesses.
    """
    api_logger.info(f"Received request for defensive weaknesses for: {type_1}, {type_2}")
    return call_and_catch(get_defensive_weaknesses, type_1, type_2)


@weaknesses_bp.route('/weaknesses/immunities/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('/weaknesses/immunities/<string:type_1>/<string:type_2>', methods=['GET'])
def bp_get_immunities(type_1: str, type_2: str = None) -> tuple[Response, int] | Response:
    """
    Retrieves all attacking pokémon types that do no damage to the given defensive types.

    :param type_1: The primary defensive pokémon type.
    :param type_2: The secondary defensive pokémon type, if applicable.
    :return: JSON response containing immunities.
    """
    api_logger.info(f"Received request for immunities for: {type_1}, {type_2}")
    return call_and_catch(get_immunities, type_1, type_2)


@weaknesses_bp.route('/weaknesses/immune-defenders/<string:type_1>', methods=['GET'])
def bp_get_immune_defenders(type_1: str) -> tuple[Response, int] | Response:
    """
    Retrieves all defensive pokémon types that are immune to the given attacking type.

    :param type_1: The attacking pokémon type.
    :return: JSON response containing immune defenders.
    """
    api_logger.info(f"Received request for immune defenders for attacker type: {type_1}")
    return call_and_catch(get_immune_defenders, type_1)


@weaknesses_bp.route('/strengths/offensive/<string:type_1>', methods=['GET'])
def bp_get_offensive_strengths(type_1: str) -> tuple[Response, int] | Response:
    """
    Retrieves all pokémon types that take extra damage from the given attacking type.

    :param type_1: The attacking pokémon type.
    :return: JSON response containing offensive strengths.
    """

    api_logger.info(f"Received request for offensive strengths for attacker type: {type_1}")
    return call_and_catch(get_offensive_strengths, type_1)


@weaknesses_bp.route('/strengths/defensive/<string:type_1>', methods=['GET'])
@weaknesses_bp.route('/strengths/defensive/<string:type_1>/<string:type_2>', methods=['GET'])
def bp_get_defensive_strengths(type_1: str, type_2: str | None = None) -> tuple[Response, int] | Response:
    """
    Retrieves all attacking pokémon types that deal reduced damage to the given defensive types.

    :param type_1: The primary defensive pokémon type.
    :param type_2: The secondary defensive pokémon type, if applicable.
    :return: JSON response containing defensive strengths.
    """

    api_logger.info(f"Received request for defensive strengths for defender type: {type_1} {type_2}")
    return call_and_catch(get_defensive_strengths, type_1, type_2)
