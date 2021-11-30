# pip install phonenumbers


import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def main(x): # x = str(number with country code), example: '+15417543010'
    x = phonenumbers.parse(x)
    y = timezone.time_zones_for_number(x)
    z = carrier.name_for_number(x, "en")
    c = geocoder.description_for_number(x, "en")
    v = f"Phone  number: {x}\nTime zone: {y}\nCarrier: {z}\nDescription: {c}"
    print(v)

