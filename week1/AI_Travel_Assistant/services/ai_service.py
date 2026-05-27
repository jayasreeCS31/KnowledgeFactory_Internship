def travel_tip(condition):

    condition = condition.lower()

    if "rain" in condition:

        tip = "Carry umbrella and waterproof bag"

        packing = [
            "Umbrella",
            "Raincoat",
            "Waterproof shoes"
        ]


    elif "clear" in condition:

        tip = "Perfect weather for sightseeing"

        packing = [
            "Sunglasses",
            "Cap",
            "Water bottle"
        ]


    elif "cloud" in condition:

        tip = "Weather may change during the day"

        packing = [
            "Light jacket",
            "Comfortable shoes",
            "Power bank"
        ]


    elif "hot" in condition:

        tip = "Stay hydrated and avoid afternoon heat"

        packing = [
            "Water bottle",
            "Sunscreen",
            "Cap"
        ]

    else:

        tip = "Enjoy your journey safely"

        packing = [
            "Phone charger",
            "ID card",
            "Basic medicines"
        ]


    return {

        "tip":tip,

        "packing":packing

    }
def travel_score(condition):

    condition=condition.lower()


    if "clear" in condition:

        return 10


    elif "cloud" in condition:

        return 8


    elif "rain" in condition:

        return 5


    return 7