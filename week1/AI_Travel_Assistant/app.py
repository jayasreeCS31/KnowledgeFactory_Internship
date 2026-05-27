from services.weather_service import get_weather
from services.place_service import get_places
from services.budget_service import estimate_budget

from services.ai_service import (
    travel_tip,
    travel_score
)

from datetime import datetime

from utils.helper import (
    save_history,
    view_history
)


while True:

    print("\n" + "="*40)

    print("     AI TRAVEL ASSISTANT")

    print("="*40)

    print("1. Plan New Trip")

    print("2. View History")

    print("3. Exit")


    choice = input(
        "\nEnter choice: "
    )


    if choice == "1":

        name = input(
            "\nEnter name: "
        )

        city = input(
            "Destination: "
        )

        try:

            days = int(
                input(
                    "Trip days: "
                )
            )

        except:

            print(
                "\nEnter valid number"
            )

            continue


        weather = get_weather(city)


        if "error" in weather:

            print(
                "\nError:",
                weather["error"]
            )


        else:

            places = get_places(
                city
            )


            budget = estimate_budget(
                days
            )


            travel = travel_tip(
                weather["condition"]
            )


            score = travel_score(
                weather["condition"]
            )


            print(
                "\n====== TRAVEL REPORT ======"
            )


            print(
                "\nWelcome",
                name
            )


            print(
                "\nWeather:",
                weather["condition"]
            )


            print(
                "Temperature:",
                weather["temperature"],
                "°C"
            )


            print(
                "Humidity:",
                weather["humidity"],
                "%"
            )


            print(
                "Travel Score:",
                score,
                "/10"
            )


            print(
                "\nRecommended Places:"
            )


            for i, p in enumerate(
                    places,
                    1
            ):

                print(
                    f"{i}. {p}"
                )


            print(
                "\nEstimated Budget:"
            )


            print(
                "₹",
                budget
            )


            print(
                "\nTravel Tip:"
            )


            print(
                "✓",
                travel["tip"]
            )


            print(
                "\nPacking Suggestions:"
            )


            for item in travel["packing"]:

                print(
                    "✓",
                    item
                )


            record = {

                "name": name,

                "city": city,

                "days": days,

                "weather": weather["condition"],

                "budget": budget,

                "date": datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )

            }


            save_history(
                record
            )


    elif choice == "2":

        view_history()


    elif choice == "3":

        print(
            "\nThank you for using AI Travel Assistant"
        )

        break


    else:

        print(
            "\nInvalid choice"
        )