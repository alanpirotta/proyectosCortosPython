import requests
#Generé la oath app en github

client_id= ''
client_scret = ''
#Ingresar a : https://github.com/login/oauth/authorize?client_id=38fbd77654bcdbdf99f9&scope=repos

#Solo funciona una vez
code = ''
access_token = ''

if __name__ == '__main__':
    
    #Para obtener al access_token
    '''
    url = 'https://github.com/login/oauth/access_token'
    payload= {'client_id': client_id, 'client_secret':  client_scret, 'code': code}
    headers = {'Accept': 'application/json'}    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_json=response.json()
        # print(response_json)
        access_token = response_json['access_token']
        print(access_token)
    '''
    
    #Obtener los repos del usuario
    '''
    url = 'http://api.github.com/user/repos'
    headers = {'Authorization': 'token '+access_token}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = response.json()
        
        for project in payload:
            name = project['name']
            print(name)
    else:
        print (response.content)
    '''
    
    #Crear un repo
    #Falla, por alguna razón retorno lo mismo que si usara un get, y no crea el repo
    url = 'http://api.github.com/user/repos'
    payload = {'name': 'repoCreadoDesdePython'}
    headers = {'Accept': 'application/json', 'Authorization': 'token '+access_token}
    
    response=requests.post(url, headers=headers, json=payload)
    print(response)
    if response.status_code == 200:
        print(payload)
        print(response.json())
    else:
        print(response.content)
    