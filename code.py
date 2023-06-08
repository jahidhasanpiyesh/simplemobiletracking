# import phonenumbers pip install and set up !

import phonenumbers
# call timezone, geocoder, carrier ?
from phonenumbers import timezone, geocoder, carrier

# input function call and numbers input ?
number = input("Enter Your Phone Numbers : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim_service = carrier.name_for_number(phone, "en")
register_location = geocoder.description_for_number(phone, "en")

print(register_location)
print(sim_service)

