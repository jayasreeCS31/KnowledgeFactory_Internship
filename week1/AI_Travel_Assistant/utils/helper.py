import json


FILE_PATH = "data/travel_history.json"


def save_history(record):

    try:

        with open(
            FILE_PATH,
            "r"
        ) as file:

            data = json.load(file)

    except:

        data=[]


    data.append(record)


    with open(
        FILE_PATH,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def view_history():

    try:

        with open(
            FILE_PATH,
            "r"
        ) as file:

            data=json.load(file)


        if len(data)==0:

            print(
                "\nNo travel history found"
            )

            return


        print(
            "\n====== TRAVEL HISTORY ======"
        )


        for i,trip in enumerate(
                data,
                1
        ):

            print(
                f"\nTrip {i}"
            )

            print(
                "Name:",
                trip["name"]
            )

            print(
                "City:",
                trip["city"]
            )

            print(f"\nTrip {i}")

            print(
                "Name:",
                trip["name"]
            )

            print(
                "Destination:",
                trip["city"]
            )

            print(
                "Days:",
                trip["days"]
            )

            print(
                "Weather:",
                trip["weather"]
            )

            print(
                "Budget:",
                "₹",
                trip["budget"]
            )

            print(
                "Date:",
                trip["date"]
            )


    except Exception as e:

        print(
            "Error:",
            e
        )