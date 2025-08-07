# PokeRouge Utility API

The **PokeRouge Utility API** is a web service designed to support various tools and utilities for Pokémon team analysis, 
aiding players in building better strategies. It currently features **Type Weakness and Strength Checkers**, 
with planned additions including **Team Checker**, **Moveset Lookup**, **Ability Lookup**, **Opposing Team Tracker**, 
and **Biome Data**.


## Features

### Currently Available

- **Type Weakness Checker**: Identify weaknesses in a single or multiple Pokémon's type combinations.
- **Type Strength Checker**: Assess which types another type can effectively cover.

### Coming Soon

- **Team Checker**: Analyze full teams for type coverage, redundancy, and synergy.
- **Moveset Lookup**: Retrieve a pokémon's available moves.
- **Ability Lookup**: Access Pokémon ability descriptions and what pokémon can have the ability.
- **Opposing Team Tracker**: Store and analyze observed enemy team compositions.
- **Biome Data Lookup**: Get Pokémon availability by biome and plot your path to get to specific biomes.
- **Interactive Front-End**: A user-friendly interface for interacting with API features.
---

## Usage

The API is currently hosted at **[https://pokerouge-util-api.onrender.com/](https://pokerouge-util-api.onrender.com/)**

You can interact with it directly via HTTP requests using tools like [Postman](https://www.postman.com/), `curl`, or through the interactive front-end (coming soon).


### Local Development

To run the API locally:
```bash
git clone https://github.com/your-username/PokeRouge-Util-API.git

cd PokeRouge-Util-API

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python3 -m Application.main
```

