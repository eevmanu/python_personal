from geopy.geocoders import GoogleV3
import geoip2.database

# Usando la libreria gratis de Python, llamando al geocoder de Google
geolocator = GoogleV3()
lat_long = '31.5184772,55.7008007'
aux = geolocator.reverse(lat_long)
print aux[len(aux)-1][0]

# Usando la libreria free de MaxMind
db_filepath = '/home/msolorzanoc/Downloads/GeoLite2-Country.mmdb'
reader = geoip2.database.Reader(db_filepath)
ip = '200.48.22.49'
response = reader.country(ip)
print response.country.name
