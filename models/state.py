#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    
    @property
    def cities(self):
        """Getter FileStorage"""
        from models.city import City
        from models import storage
        
        cities = []
        
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities

    
    