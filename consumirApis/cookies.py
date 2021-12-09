import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = { 'cookie1': 'true'}
    
    response = requests.get(url, cookies=cookies)
    
    if response.ok:
        cookies = response.cookies
        print(cookies)
        
        print('Contenido:')
        print(response.text)