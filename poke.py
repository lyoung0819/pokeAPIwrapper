import requests
from ascii_magic import AsciiArt


class PokemonDeets:    
    
    def __init__(self, name, height, weight, image):
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.image = image

    def __str__(self):
        art = AsciiArt.from_url(self.image)
        art_str = art.to_ascii()
        return f"""
        {self.name}: 
        height: {self.height}
        weight: {self.weight}
        {art_str}
        """
    
class PokemonAPI:
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    
    # setting up the get request blueprint of how to interact with the endpoint url 
    def __get(self, name):
        request_url = self.base_url + name
        response = requests.get(request_url)
        if response.ok:
            data = response.json() #make sure its json data
            return data
        else:
            return None

    # method to get pokemon info
    def get_pokemon_deets(self, poke_name):
        pokemon_data = self.__get(poke_name.lower())
        if pokemon_data: #as long as there is data...
            name = pokemon_data.get('name')
            height = pokemon_data.get('height')
            weight = pokemon_data.get('weight')
            image = pokemon_data.get('sprites').get('front_default')
            poke_obj = PokemonDeets(name, height, weight, image) 
            return poke_obj
        else:
            print(f'I\'m sorry, we could not find data on {poke_name}')



def main():
    client = PokemonAPI()
    print('Welcome to our Pokemon database!')
    while True:
        poke = input('Please enter your Pokemon\'s name you would like to search for: ')
        if poke == 'quit':
            break
        pokemon = client.get_pokemon_deets(poke)
        print(pokemon)


main()