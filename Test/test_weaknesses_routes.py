from unittest.mock import patch

import pytest
from flask import Response

from Application.Utils.TypeUtils import TypeUtils

type_util: TypeUtils = TypeUtils()


def assert_empty_response(client, route: str):
    expected_response: None = None
    actual: Response = client.get(f'/weaknesses/{route}')

    assert actual.json == expected_response
    assert actual.status_code == 404


def test_incomplete_weakness_route(client):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/')

    assert actual.json == expected_response
    assert actual.status_code == 404


# ============================================================
# /weaknesses/summary/<pokemon>
# ============================================================

def test_get_weakness_summary_pokemon_empty_str(client):
    assert_empty_response(client, '/weaknesses/')


def test_get_weakness_summary(client):
    expected_summary: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
        "offensive_strengths": {"grass": sorted(["ground", "rock", "water"]),
                                "poison": sorted(["grass", "fairy"])},
        "defensive_strengths": sorted(["fighting", "water", "electric", "fairy", "grass"])
    }

    actual: Response = client.get('/weaknesses/summary/bulbasaur')

    assert expected_summary == actual.json
    assert actual.status_code == 200


def test_get_weakness_summary_mixed_case(client):
    expected_summary: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
        "offensive_strengths": {"grass": sorted(["ground", "rock", "water"]),
                                "poison": sorted(["grass", "fairy"])},
        "defensive_strengths": sorted(["fighting", "water", "electric", "fairy", "grass"])
    }

    actual: Response = client.get('/weaknesses/summary/bUlBaSaUr')

    assert expected_summary == actual.json
    assert actual.status_code == 200


def test_get_weakness_summary_pokemon_not_found(client):
    expected_response: dict[str, str] = {"message": "Pokemon not found"}
    actual: Response = client.get('/weaknesses/summary/bulba')

    assert expected_response == actual.json
    assert actual.status_code == 404


@patch("Application.Routes.Weakness.TypeUtils.get_weakness_strength_summary",
       return_value={"error": "'Sound' is not a valid type"})
def test_get_mock_get_summary(mock_type_util, client):
    expected_response: dict[str, str] = {"error": "'Sound' is not a valid type"}
    actual: Response = client.get('/weaknesses/summary/bulbasaur')

    mock_type_util.assert_called_once()
    assert actual.json == expected_response
    assert actual.status_code == 400


def test_get_weakness_summary_pokemon_empty_space(client):
    expected_response: dict[str, str] = {"message": "Pokemon not found"}
    actual: Response = client.get('/weaknesses/summary/ ')

    assert actual.json == expected_response
    assert actual.status_code == 404


# ============================================================
# Mono-type tests
# ============================================================

valid_types: list = list(type_util.types.keys()) + ['FiRe', 'FIRE']
route_methods: dict = {
    "weaknesses/offensive": type_util.get_offensive_weaknesses,
    "weaknesses/defensive": type_util.get_defensive_weaknesses,
    "weaknesses/immunities": type_util.get_immunities,
    "weaknesses/immune-defenders": type_util.get_immune_defenders,
    "strengths/offensive": type_util.get_offensive_strengths,
    "strengths/defensive": type_util.get_defensive_strengths
}
dual_type_routes = ["weaknesses/defensive", "weaknesses/immunities", "strengths/defensive"]


@pytest.mark.parametrize("route", route_methods.keys())
@pytest.mark.parametrize('valid_type', valid_types)
def test_valid_inputs(client, route: str, valid_type: str):
    """Tests all weaknesses routes with valid inputs"""
    subject = route_methods[route]

    if route in dual_type_routes:
        expected_list: list = subject(valid_type, None)

    else:
        expected_list: list = subject(valid_type)
    expected_status: int = 200

    response: Response = client.get(f'/{route}/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("route", route_methods.keys())
@pytest.mark.parametrize("bad_route", ["", "/", "fire/grass"])
def test_bad_route(client, route: str, bad_route: str):
    assert_empty_response(client, f'/{route}/{bad_route}')


@pytest.mark.parametrize("route", route_methods.keys())
@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_invalid_types(client, route: str, invalid_type: str):
    """Tests all monotype weaknesses routes with invalid inputs"""
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/{route}/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message


# ============================================================
# Dual-type tests
# ============================================================


@pytest.mark.parametrize("route", dual_type_routes)
@pytest.mark.parametrize('valid_type_1', ["fire", "ghost", "fIrE"])
@pytest.mark.parametrize('valid_type_2', valid_types)
def test_valid_inputs_dual_type(client, route: str, valid_type_1: str, valid_type_2: str):
    """Tests dual type routes with valid inputs"""
    subject = route_methods[route]

    expected_list: list = subject(valid_type_1, valid_type_2)
    expected_status: int = 200

    response: Response = client.get(f'/{route}/{valid_type_1}/{valid_type_2}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("route", dual_type_routes)
@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_invalid_types(client, route: str, invalid_type: str):
    """Tests all dual-type weaknesses routes with invalid inputs"""
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/{route}/fire/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message
