import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #busca la request
    print(r.status_code) #estado
    print(r.text)  #muestra todo el texto
    print(type(r.text)) # muestra el formato
    categories = r.json() #lo convierte en un json
    for category in categories: 
        print(category['name'])