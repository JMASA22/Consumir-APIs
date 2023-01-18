import requests

apiKey = "4F68B055-356A-40B3-9241-36E93EE62298"
moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()# upper método mayúsculas()

while moneda_cripto != "" and moneda_cripto.isalpha():#método para comprobar valor numérico

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

    #print(r.status_code)

    #print(r.text)

    #ej 1: capturar resultados correctos
    resultado = r.json() #guardamos r.json en resultado (diccionarios de pyhton)
    if r.status_code == 200:
        #valor = round(resultado["rate"], 4) / print(f"{valor} €")
        #ej3: formateamos el valor rate en €
        print("{:.2f}€".format(resultado["rate"]))
    #ej 2: capturar errores
    else:
        print(resultado["error"])

    #ej 4: controlar input vacio, q no realize consulta si el input está vacio
    moneda_cripto = input ("Ingrese una criptomoneda conocida").upper()
