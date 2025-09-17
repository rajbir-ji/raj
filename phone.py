import phonenumbers
from phonenumbers import geocoder, carrier

numbers = [
    "+14082747378",
    "+61724375187",
    "+41728424692",
    "+917986805005",
]

print("\nPhone number location and carrier info\n")
for num in numbers:
    phone_number = phonenumbers.parse(num)
    location = geocoder.description_for_number(phone_number, "en")
    service_provider = carrier.name_for_number(phone_number, "en")
    print(f"Number: {num}")
    print(f"Location: {location}")
    print(f"Carrier: {service_provider}\n")