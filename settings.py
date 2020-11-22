DEBUG = True

# Data source API key
APIKEY = "b7408a982e252e37009ffee025cbbf22"

# Data source API URL
WEATHER_API = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# Data source fetch interval
REFRESH_MIN = 1  # minutes

# Cities fetched
CITIES = [
    "Montreal",
    "Quebec",
    "Sherbrooke",
]

REST_API_IP = "0.0.0.0"
REST_API_PORT = 5000

LOG_FORMAT = "%(asctime)-15s - %(levelname)s - %(message)s"
