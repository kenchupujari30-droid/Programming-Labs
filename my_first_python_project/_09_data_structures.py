"""
_09_data_structures.py

Lists, dictionaries, tuples, and the combination that matters most
later: a list of dictionaries. Still zero mention of AI or agents.

Run with: uv run _09_data_structures.py
"""

# --- Lists: an ordered, changeable collection ---
cities = ["Tokyo", "Bangalore", "Londan", "Gulbarga"]
print(cities[0])                         # indexing------- first item
print(cities[-1])                        # negative indexing------- last item
print(cities[0:2])                       # slicing ----- a sub list
cities.append("Paris")                   # adding to the end
print(cities)

for city in cities:
  print(f"visiting :{city}")

  # --- Tuples: like a list, but cannot be changed after creation ---

coordinates = (35.68,139.69)          # latitude, longitude -- a fixed pair
lattitude, longitude = coordinates    # unpacking --splitting a tuple into separate variables
print(f"Lat: {lattitude}, Lon:{longitude}")

# --- Dictionaries: labeled data, accessed by key instead of position ---

weather_reading = {
  "city": "Tokyo",
  "temperature_c": "22.5",
  "condition": "partialy cloudy"
}
print(weather_reading["city"])             #access by key
print(weather_reading.get("humidity"))     #.get() returns None instead of crassing if missing
weather_reading["humidity"]= 60
print(weather_reading)

for key, value in weather_reading.items():
  print("f{key}: {value}")

## --- The combination that matters most: a list of dictionaries ---

readings = [
  {"city": "Tokyo", "temperature_c":22.5},
  {"city": "Bangalore", "temperature_c":34.0},
  {"city": "London", "temperature_c":15.0},
]
for reading in readings:
  print(f"{reading['city']},{reading['temperature_c']}°C")

warm_cities = [r ["city"] for r in readings if r["temperature_c"] > 20 ]  #list comprehension
print(f"warm cities: {warm_cities}")

if __name__ == "__main__":
    print("\nData structures done. Still nothing AI-related -- next up, OOP.")