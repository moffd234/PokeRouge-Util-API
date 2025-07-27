from flask import Flask

from Application.Models.Types import Types


class WeaknessService:

    @staticmethod
    def get_type_data(type_name: str) -> Types:
        cleaned_type: str = type_name.upper().strip()
        try:
            return Types[cleaned_type]
        except KeyError:
            raise ValueError(f"Unknown type: {type_name}")

    @staticmethod
    def get_offensive_weaknesses(type_1: Types) -> list[str]:
        return type_1.offensively_weak

