import requests
import json

if __name__ == '__main__':
    url= 'https://i.imgur.com/NMhO55j.jpeg'
    
    #El stream hace que no cierre la conexión
    response= requests.get(url,stream=True)
    with open ('image.jpg', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    response.close()