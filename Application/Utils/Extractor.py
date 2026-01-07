import json
import logging
import re

import requests

POKEMON_SPECIES_TS_URL = "https://raw.githubusercontent.com/pagefaultgames/pokerogue/beta/src/data/pokemon-species.ts"

# Field names come from the pokemonSpecies constructor in the Pokerouge source file above
FIELD_NAMES = [
    "id",
    "generation",
    "subLegendary",
    "legendary",
    "mythical",
    "category",
    "type1",
    "type2",
    "height",
    "weight",
    "ability1",
    "ability2",
    "abilityHidden",
    "baseTotal",
    "baseHp",
    "baseAtk",
    "baseDef",
    "baseSpatk",
    "baseSpdef",
    "baseSpd",
    "catchRate",
    "baseFriendship",
    "baseExp", "growthRate", "malePercent", "genderDiffs", "canChangeForm"
]

extractor_logger = logging.getLogger("utils.extractor")


def extract_species_blocks(source):
    pattern = re.compile(r'new\s+PokemonSpecies\s*\((.*?)\)\s*,?', re.DOTALL)
    return pattern.findall(source)


def clean_and_split_args(arg_str):
    args = []
    current = ""
    depth = 0
    for char in arg_str:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if char == ',' and depth == 0:
            args.append(current.strip())
            current = ""
        else:
            current += char
    if current:
        args.append(current.strip())
    return args


def parse_simple_value(val):
    val = val.strip()

    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]

    if val.isdigit():
        return int(val)
    try:
        return float(val)
    except ValueError:
        pass

    if val == "true":
        return True
    if val == "false":
        return False
    if val == "null":
        return None

    prefixes = ["PokemonType.", "AbilityId.", "SpeciesId.", "GrowthRate."]
    for prefix in prefixes:
        if val.startswith(prefix):
            return val[len(prefix):]

    return val


def main():
    try:
        source = requests.get(POKEMON_SPECIES_TS_URL).text

    except requests.exceptions.RequestException as error:
        extractor_logger.critical(f"Failed to get species data from pokerouge repo: {error}", exc_info=True)
        return

    species_blocks = extract_species_blocks(source)

    all_species = []
    for block in species_blocks:
        args = clean_and_split_args(block)
        species = {}

        for i, arg in enumerate(args):
            key = FIELD_NAMES[i] if i < len(FIELD_NAMES) else f"extraArg{i}"
            species[key] = parse_simple_value(arg)

        all_species.append(species)

    with open("../Data/pokemon_species.json", "w", encoding="utf-8") as f:
        json.dump(all_species, f, indent=4, ensure_ascii=False)

    extractor_logger.info(f"Extracted {len(all_species)} Pokémon species into pokemon_species.json")


if __name__ == "__main__":
    main()
