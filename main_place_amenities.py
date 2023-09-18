#!/usr/bin/python3
"""
Test link Many-To-Many Place <> Amenity
"""
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


# Creation of a State
state = State(name="California")
state.save()

# Creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# Creation of a User
user = User(email='john@snow.com', password='johnpwd')
user.save()

# Creation of 2 places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# Createion of 3 various Amenities
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# Link place_1 with 2 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)
place_2.save()
# place_2.save() - it doesn't save on its own

storage.save()

print("OK")
