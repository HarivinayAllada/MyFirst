# importing phonenumbers module
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

# to get the input(phone number) from the user
Phone_Number = phonenumbers.parse(input("Enter your phone number with country code : "))

#to get the time zone of a phone number
Time_Zone = timezone.time_zones_for_number(Phone_Number)

# to get carrier of a phone number
Carrier = carrier.name_for_number(Phone_Number,"en")

#to get region of the phone number
Region = geocoder.description_for_number(Phone_Number,"en")

#to check phone number is valid or not
check = phonenumbers.is_valid_number(Phone_Number)

print(Phone_Number)
print(Time_Zone)
print(Carrier)
print(Region)
print("phone number is vald : ",check)
