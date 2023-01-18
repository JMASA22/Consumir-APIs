import requests
from utils import apiKey

r = requests.get(f'https://rest.coinapi.io/v1/asset/?apikey={apiKey}')
if r.status_code == 200:
    raise Exception ("Error en consulta de assets:{}".format(r.status_code))

lista_general = r.json()
lista_criptos = []

for item in lista_general:
    if item ["type_is_crypto"] == 1:
        lista_criptos.append(item["asset_id"])

moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()# upper método mayúsculas()

while moneda_cripto != "" and moneda_cripto.isalpha():#método para comprobar valor numérico
   
    if moneda_cripto in lista_criptos:
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

        #capturar resultados correctos
        resultado = r.json() #guardamos r.json en resultado (diccionarios de pyhton)
        if r.status_code == 200:
            print("{:.2f}€".format(resultado["rate"])) #formateamos el valor rate en €
        else:
            print(resultado["error"])

    moneda_cripto = input ("Ingrese una criptomoneda conocida").upper() #q no realize consulta si el input está vacio
