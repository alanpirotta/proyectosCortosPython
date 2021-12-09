import requests

if __name__ == '__main__':
    url = 'http://api.github.com/user'
    
    session = requests.session()
    session.auth = ('','')
    
    response = session.get(url)
    if response.ok:
        print(response.text)
    else:
        print("Fallo", response)
        
#No funciona la auntenticación