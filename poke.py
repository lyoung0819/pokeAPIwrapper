import requests # type: ignore

class PokemonDeets:    
    def __init__(self, name, height, weight, abilities, stats):
        self.name = name
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.stats = stats

    def __str__(self):
        return f"""
        {self.name} : 
        height: {self.height}
        weight: {self.weight}
        abilities: {self.abilities}
        stats: {self.stats}"""
    


class PokemonAPI:
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    
    # setting up the get request blueprint of how to interact with the endpoint url 
    def __get(self, name):
        self.name = name
        request_url = f"{self.base_url}{self.name}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        
    # method to get pokemon info
    def get_pokemon_deets(self, name):
        pokemon_data = self.__get(name)
        if pokemon_data:
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            abilities = pokemon_data['abilities']['abilities']['name']
            stats = pokemon_data['stats']['base_stat']
        else:
            print('I\'m sorry, we could not find data on {self.name}')

    
def main():
    print('Welcome to our Pokemon database!')
    client = PokemonAPI
    name = input("Please enter your Pokemon's name you would like to search for:   ").lower()
    poke_info = client.get_pokemon_deets(name)
    print(poke_info)

main()