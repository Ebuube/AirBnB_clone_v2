#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import (Column, String, Integer, Float, ForeignKey, Table)
from sqlalchemy.orm import relationship


"""
An association table between the 'Place' and 'Amenity' models
"""
if isinstance(models.storage, models.DBStorage):
    place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay

    Attributes:
        city_id:(str)empty string: it will be the City.id
        user_id: (str)empty string: it will be the User.id
        name: (str) empty string
        description: (str) empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude:float - 0.0
        amenity_ids:list of string -empty list: it will be
        the list of Amenity.id later
    """
    __tablename__ = 'places'

    if isinstance(models.storage, models.DBStorage):
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=(0))
        number_bathrooms = Column(Integer, nullable=False, default=(0))
        max_guest = Column(Integer, nullable=False, default=(0))
        price_by_night = Column(Integer, nullable=False, default=(0))
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship('Review', backref='place',
                               cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Return a list of 'Review' instances linked to this Place
            """
            objs = list()
            if objs is None:
                return list()

            for obj in models.storage.all(City).values():
                if obj.place_id == self.id:
                    objs.append(obj)

            return objs

        @property
        def amenities(self):
            """
            Return a list of 'Amenity' instances linked to this place object
            """
            from models.amenity import Amenity

            objs = list()
            for obj in storage.all(Amenity).values():
                if obj.place_id == self.id:
                    objs.append(obj)

            return objs

        @amenities.setter
        def amenities(self, obj):
            """
            Add the id of an Amenity object to self.amenity_ids

            NOTE: This method accepts only Amenity objects,
            otherwise it does nothing
            """
            from models.amenity import Amenity
            from models import storage

            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
                self.save()
                obj.save()
                # storage.new(self)
                # storage.save()
