import weatherAPI
import DatabaseConnection


def main():
    response = weatherAPI.get_weather("/current.json")
    current = response["current"]
    condition = current["condition"]
    DatabaseConnection.create_condition(
        condition["code"],
        condition["text"],
        condition["icon"],
    )

    DatabaseConnection.create_day_weather(
        current["temp_c"],
        current["wind_kph"],
        current["wind_degree"],
        current["wind_dir"],
        current["feelslike_c"],
        condition["code"]
    )


if __name__ == '__main__':
    main()
