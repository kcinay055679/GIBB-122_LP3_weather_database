import mariadb


def get_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="password",
            host="127.0.0.1",
            port=3306,
            database="weather"
        )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None
    return conn.cursor()


def create_day_weather(temp_c, wind_kph, wind_degree, wind_direction, temp_c_feels_like, condition_code):
    cur = get_connection()
    if cur is None:
        return
    cur.execute(
        "INSERT ignore INTO day_weather "
        "(temp_c, wind_kph, wind_degree, wind_direction, temp_c_feels_like, condition_code) VALUES "
        "(?, ?, ?, ?, ?, ?)",
        (temp_c, wind_kph, wind_degree, wind_direction, temp_c_feels_like, condition_code))


def create_condition(code, text, icon_link):
    cur = get_connection()
    if cur is None:
        return

    cur.execute("INSERT ignore INTO conditions (condition_code, text, icon_link) "
                "VALUES (?, ?, ?)", (code, text, icon_link))
