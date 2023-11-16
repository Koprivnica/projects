from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

@dataclass
class Coordinates:
    latitude: float
    longitude: float
    
    def coordinates(self):
        return self.latitude, self.longitude

def get_coordinates(address: str) -> Coordinates or None:
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(address)
    
    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)

def calculate_distance_km(home: Coordinates, target: Coordinates) -> float or None:
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        
        return distance

def get_distance_km(home: str, target: str) -> float or None:
    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)
    
    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f"{home} ---> {target}")
        print(f"{distance:.2f} kilometres")
        return distance
    else:
        print("Failed to calculate the distance")

def main():
    home_address: str = "Faberstrasse 8, Munich 81373, Germany"
    print(f"Home address: {home_address}")
    
    target_address: str = input("Enter an address: ")
    print("Calculating...")
    get_distance_km(home_address, target_address)

if __name__ == "__main__":
    main()