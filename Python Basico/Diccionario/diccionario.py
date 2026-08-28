my_hotel = {
    "name": "Sebastian's Hotel",
    "stars": 5,
    "rooms": [
        {
            "number": 1,
            "floor": 2,
            "price_per_night": 200
        },
        {
            "number": 5,
            "floor": 3,
            "price_per_night": 500
        }
    ]
}

print(my_hotel.get('rooms'))