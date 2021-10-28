from dataclasses import dataclass

@dataclass
class Listing:
    id:str
    name:str
    lat:float
    lng:float
    table = "Listings"

@dataclass
class Availability:
    id:str
    date:str
    available:bool
    maxNights:int
    minNights:int
    availableForCheckin:bool
    availableForCheckout:bool
    bookable:bool
    table = "Availability"



@dataclass
class BasicListItem:
    amenity:str

@dataclass
class Pictures:
    id:str
    url:str

