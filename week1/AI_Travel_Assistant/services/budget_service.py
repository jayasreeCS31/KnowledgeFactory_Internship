def estimate_budget(days):

    hotel = 1500
    food = 700
    transport = 500

    total = (
        hotel +
        food +
        transport
    ) * days

    return total