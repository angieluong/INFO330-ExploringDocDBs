import sqlite3  # This is the package for all sqlite3 access in Python
from pymongo import MongoClient

# Connect to MongoDB - Provided in lab
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

conn = sqlite3.connect('./pokemon.sqlite')
cursor = conn.cursor()

general_query = """
SELECT name, pokedex_number, hp, attack, defense, speed,
sp_attack, sp_defense
FROM pokemon
"""
cursor.execute(general_query)

for row in cursor.fetchall():
    name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense = row
    abilities_query = """
    SELECT ability.name, pokemon.pokedex_number
    FROM ability
    JOIN pokemon_abilities ON pokemon_abilities.ability_id = ability.id
    JOIN pokemon ON pokemon_abilities.pokemon_id = pokemon.id
    WHERE pokedex_number = ?
    """
    abilities = [name[0] for name in conn.execute(abilities_query, (pokedex_number,))]
    cursor.execute("SELECT * FROM pokemon_types_view WHERE name = ?", (name,))
    pokemon_type_info = cursor.fetchone()

    type_1 = pokemon_type_info[1]
    type_2 = pokemon_type_info[2]

    pokemon = {
        "name": name,
        "pokedex_number": pokedex_number,
        "types": [type_1, type_2],
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "speed": speed,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "abilities": abilities,
    }

    pokemonColl.insert_one(pokemon)

conn.close()
mongoClient.close()