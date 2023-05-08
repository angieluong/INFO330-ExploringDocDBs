import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    pokemon1_points = 0

    pokemon2_points = 0

# Whichever pokemon has the superior stat for each category will get points added to their total
    for stat in ['hp', 'attack', 'defense', 'speed']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1_points += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2_points += 1

# Special Attacks and Defenses are ~special~, so they cause more variation in points!
    for stat in ['sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1_points += 2
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2_points += 2

# Whichever Pokemon has more points wins
# If they get the same amount of points, there is a tie
# I also added more commentary
    if pokemon1_points > pokemon2_points:
        print("Battle results: " + pokemon1['name'] + " wins!")
        print(pokemon2['name'] + " will get them next time....")
    elif pokemon2_points > pokemon1_points:
        print("Battle results: " + pokemon2['name'] + " wins!")
        print(pokemon1['name'] + " will get them next time....")
    else:
        print("Battle results: it's a tie :o")

# Original Battle Results Code
    # winner = random.randrange(2)
    # if winner == 0: print("Battle results: " + pokemon1['name'])
    # if winner == 1: print("Battle results: " + pokemon2['name'])

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
