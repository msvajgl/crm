import json

# Load JSON file
with open("filtered_station.json", encoding="utf-8") as f:
    data = json.load(f)

# Count total number of stations
# Each object in "records" represents a station
total_stations = len(data.get("records", []))

print(f"Total number of stations: {total_stations}")
