def format_itineraries(flight_list):
    formatted_itineraries = [
        f"Itinerary {i + 1}: {traveler_name} - From {origin} to {destination}"
        for i, (traveler_name, origin, destination) in enumerate(flight_list)
    ]
    
    return "\n".join(formatted_itineraries)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
result = format_itineraries(itineraries)
print(result)