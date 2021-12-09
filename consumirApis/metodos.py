import requests
import json

if __name__ == '__main__':
#Método GET
    '''
    url = 'http://httpbin.org/get'
    #Al agregarlo como params en el request, los agrega directo como si fuera:
    # http://httpbin.org/get?nombre=Alan&apellido=Pirotta
    args = {
        'nombre': 'Alan',
        'apellido': 'Pirotta'
    }
    response = requests.get(url, params=args)
    
    # print(response)  #200 es correcto
    
    if response.status_code == 200:
        #Para crear un archivo con el contenido del response del get
        content= response.content
        file = open ('google.html', 'wb')
        file.write(content)
        file.close()
        #Si uso content, me devuelve un byte que dice b al ppio
        #content = response.content
        content = response.text
        #agrego el decode para eliminar el b del inicio que indica que es un byte object
        # print(content.decode('utf-8'))
        print(content)
        
        # response_json = response.json()
        # origin = response_json['origin']
        # print(origin)
        
        #Con librería json
        response_json=json.loads(response.text)
        #puedo poner cualquiera de las keys
        origin = response_json['origin']
        print(origin)
        print(json.dumps(response_json, indent=2))
    '''
        
#Método POST, PUT y DELETE
    '''
    # url = 'http://httpbin.org/post'
    # url = 'http://httpbin.org/put'
    url = 'http://httpbin.org/delete'
    payload = {
        'nombre': 'Daniela',
        'Apellido': 'Serra'
    }
    headers={
        'content-Type': 'application/json',
        'access-token': '123456789'
    }
    # response = requests.post(url,json=payload)
    # response = requests.put(url,json=payload)
    response = requests.delete(url,json=payload)
    # print(response.url)
    
    if response.status_code == 200:
        # print (response.text)
        headers_response=response.headers
        # print(headers_response)
        server = headers_response['Server']
        print(server)
    '''


