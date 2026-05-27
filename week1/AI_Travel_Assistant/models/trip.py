class Trip:

    def __init__(
            self,
            destination,
            days
    ):

        self.destination = destination
        self.days = days


    def show_trip(self):

        print(
            "Destination:",
            self.destination
        )

        print(
            "Days:",
            self.days
        )