from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu"
def pikachu():
    pikachu = pokemonColl.find_one({"name": "Pikachu"}, projection={"_id": False})
    print(pikachu)

# Write a query that returns all the Pokemon with an attack greater than 150
def greater_than_150():
    greater_than = pokemonColl.find({"attack": {"$gt": 150}})
    for pokemon in greater_than:
        print(pokemon)


# Write a query that returns all the Pokemon with an ability of "Overgrow"
def overgrow():
    overgrow_ability = pokemonColl.find({"abilities": {"$in": ["Overgrow"]}})
    for pokemon in overgrow_ability:
        print(pokemon)

pikachu()
greater_than_150()
overgrow()


mongoClient.close()