import requests
r = requests.get('https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=4F68B055-356A-40B3-9241-36E93EE62298')
print(r.status_code)
print(r.text)