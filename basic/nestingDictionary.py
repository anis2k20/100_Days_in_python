travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Bangladesh",
        "cities_visited": ["Dhaka", "Jamalpur", "Rajshahi"],
        "total_visits": 8,
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = (country_visited,)
    new_country["total_visits"] = (times_visited,)
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Seint Petersburg"])
print(travel_log)
