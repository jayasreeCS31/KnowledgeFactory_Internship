places = {

    "hyderabad": [
        "Charminar",
        "Golconda Fort",
        "Ramoji Film City",
        "Hussain Sagar",
        "Birla Mandir",
        "Nehru Zoological Park",
        "Chowmahalla Palace",
        "Salar Jung Museum"
    ],

    "delhi": [
        "India Gate",
        "Red Fort",
        "Qutub Minar",
        "Lotus Temple",
        "Akshardham Temple",
        "Humayun's Tomb",
        "Jama Masjid",
        "Rashtrapati Bhavan"
    ],

    "mumbai": [
        "Gateway of India",
        "Marine Drive",
        "Juhu Beach",
        "Elephanta Caves",
        "Siddhivinayak Temple",
        "Bandra-Worli Sea Link",
        "Haji Ali Dargah",
        "Sanjay Gandhi National Park"
    ],

    "vijayawada": [
        "Kanaka Durga Temple",
        "Bhavani Island",
        "Undavalli Caves",
        "Prakasam Barrage",
        "Gandhi Hill",
        "Rajiv Gandhi Park",
        "Subramanya Swamy Temple"
    ],

    "guntur": [
        "Amaravati",
        "Uppalapadu Bird Sanctuary",
        "Kondaveedu Fort",
        "Mangalagiri Temple",
        "Ethipothala Waterfalls",
        "Suryalanka Beach",
        "Haailand"
    ],

    "chennai": [
        "Marina Beach",
        "Kapaleeshwarar Temple",
        "Mahabalipuram",
        "Valluvar Kottam",
        "Guindy National Park"
    ],

    "bangalore": [
        "Lalbagh Botanical Garden",
        "Cubbon Park",
        "Bangalore Palace",
        "Wonderla",
        "ISKCON Temple"
    ],

    "kolkata": [
        "Victoria Memorial",
        "Howrah Bridge",
        "Dakshineswar Temple",
        "Science City",
        "Eco Park"
    ],

    "goa": [
        "Baga Beach",
        "Calangute Beach",
        "Dudhsagar Falls",
        "Fort Aguada",
        "Basilica of Bom Jesus"
    ],

    "jaipur": [
        "Hawa Mahal",
        "Amber Fort",
        "City Palace",
        "Jal Mahal",
        "Nahargarh Fort"
    ]
}


def get_places(city):
    city = city.lower()
    return places.get(
        city,
        ["No tourist data available"]
    )