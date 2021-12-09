import requests

def get_pokemon (url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = { 'offset': offset} if offset else {}
    
    response = requests.get(url, params=args)

    if response.status_code == 200:
        
        payload = response.json()
        listado = payload.get('results', [])
        
        if listado:
            for pokemon in listado:
                nombre=pokemon['name']
                print(nombre)
                
        next = input("Continuear con el listado? Y/N: ").lower()
        if next == 'y':
            offset+=20
            get_pokemon(offset=offset)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    get_pokemon()