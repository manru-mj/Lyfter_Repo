hotel_info = {
'name': 'Imaginary Hotel',
'stars': 5,
'rooms': 
    [
    {
    'number': 1,
    'floor' : 1,
    'cost_per_night': '$150'
    },
    {
    'number': 2,
    'floor' : 1,
    'cost_per_night': '$175'
    },
    {
    'number': 3,
    'floor' : 2,
    'cost_per_night': '$200'
    },
    {
    'number': 4,
    'floor' : 2,
    'cost_per_night': '$250'
    }
]
}

print(f"room number: {hotel_info['rooms'][2]['number']}")
print(f"floor number: {hotel_info['rooms'][2]['floor']}")
print(f"cost per night: {hotel_info['rooms'][2]['cost_per_night']}")

