import phonenumbers
import folium

from myNumber import number
from phonenumbers import geocoder
Key="b1fa1b7224a9430ca8d1bd54411bb189"
someNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(someNumber, "en")
print(yourLocation)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)
Query = str(yourLocation)
results = geocoder.geocode(Query)
##print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat ,lng],popup=yourLocation).add_to((myMap))

myMap.save("myLocation.html")

