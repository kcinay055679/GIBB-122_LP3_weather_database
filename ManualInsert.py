import re
import DatabaseConnection
REGEX_TEMPERATURE = "^-?[0-9]{1,3}.[0-9]{2}"
REGEX_DEGREE = "^[1-3]?[0-9]?[0-9]$|^[3][0-5][0-9]$|^[3][6][0]$"


def create_day_weather_manual():
    temp_c = validate_parameter("Insert the temp in celsius", REGEX_TEMPERATURE)
    wind_kph = validate_parameter("Insert wind speed in kph", "[0-9]{3}")
    wind_degree = validate_parameter("Insert wind degree in", REGEX_DEGREE)
    wind_direction = validate_parameter("Insert the temp in celsius", "(N|E|W|S){,3}")
    temp_c_feels_like = validate_parameter("Insert the feels like temp in celsius", REGEX_TEMPERATURE)
    condition_code = validate_parameter("Insert the condition code", "[0-9]{4}")

    DatabaseConnection.create_day_weather(temp_c, wind_kph, wind_degree,
                                          wind_direction, temp_c_feels_like, condition_code)


def check_manual_insert():
    while True:
        result = input("Do you want to insert data manually? (y/n)")
        if result == "y" or result == "n":
            return result == "y"


def validate_parameter(parameter_description, regex_pattern):
    while True:
        result = input(parameter_description)

        x = re.findall(regex_pattern, result)
        if len(x) > 0:
            return x
