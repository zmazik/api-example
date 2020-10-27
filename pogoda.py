"""
Przykład synchronicznego pobierania danych z api.
Prosty program służący do pobrania prognozy pogody domyślnie dla Bielska-Białej na następny dzień z serwisu AccuWeather.
Mikołaj Kubiczek, 2020
"""

# Należy wczytać odpowiednie biblioteki
import os
from dotenv import load_dotenv
import requests

# Wczytujemy klucz api
load_dotenv()
key = os.getenv('API_KEY')

# Przygotujmy lokalizację
p = float(input('Długość geograficzna (domyślnie dla Bielska-Białej)') or 49.8224)
q = float(input('Szerokość geograficzna (domyślnie dla Bielska-Białej)') or 19.0584)

# Otrzymujemy id lokalizacji
location_id = requests.get(url="http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={}&q={},{}".format(key, p, q)).json()['Key']

# Przygotowujemy żądanie HTTP i otrzymujemy odpowiedź
response = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}?apikey={}&language=pl&details=true&metric=true".format(location_id, key)).json()
tommorow = response['DailyForecasts'][0]

print() # Linijka przerwy

# Wypisujemy dane
print(response['Headline']['Text'])
print('Temperatura:')
print('- min. {} C'.format(tommorow['Temperature']['Minimum']['Value']))
print('- max. {} C'.format(tommorow['Temperature']['Maximum']['Value']))
print('- odczuwalna min. {} C'.format(tommorow['RealFeelTemperature']['Minimum']['Value']))
print('- odczuwalna max. {} C'.format(tommorow['RealFeelTemperature']['Maximum']['Value']))
print(tommorow['Day']['IconPhrase'])
print('Wiatr {} km/h {}'.format(tommorow['Day']['Wind']['Speed']['Value'], tommorow['Day']['Wind']['Direction']['Localized']))
