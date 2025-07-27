from Application.Models.Types import Types
from Application.Services.WeaknessService import WeaknessService


def test_weakness_fire():
    expected: list[str] = ["Fire", "Grass", "Ice", "Steel", "Fairy", "Bug"]
    actual: list[str] = WeaknessService.get_offensive_weaknesses(Types.FIRE)

    assert actual == expected