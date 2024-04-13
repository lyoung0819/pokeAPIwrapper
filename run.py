from poke import PokemonAPI


def main():
    print('Welcome to our Pokemon database!')
    client = PokemonAPI
    name = input("Please enter your Pokemon's name you would like to search for:   ").lower()
    poke_info = client.get_pokemon_deets(name)
    print(poke_info)

main()