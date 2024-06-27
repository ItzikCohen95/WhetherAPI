# WeatherAPI

WeatherAPI is a simple Flask application that provides weather data for a given city using the Weatherbit API.

## Getting Started

These instructions will help you set up and run the WeatherAPI on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- requests

### Installing

1. Clone the repository:

```bash
git clone https://github.com/ItzikCohen95/WhetherAPI.git
cd WhetherAPI
```

2. Install the required packages:

```bash
pip install Flask requests
```

### Running the Application

1. Set the API key for the Weatherbit API in the `project.py` file.

2. Run the Flask application:

```bash
python project.py
```

3. The application will be running on `127.0.0.1:5000/`.

### Using the API

To get weather data for a city, send a GET request to `/weather` with the `city` query parameter.

Example:

```bash
curl 127.0.0.1:5000/weather?city=London
```

The response will be a JSON object containing the weather data for the specified city.

### Example Response

```json
{
  "data": [
    {
      "city_name": "London",
      "temp": 15.6,
      "weather": {
        "description": "Partly cloudy"
      }
    }
  ]
}
```

### Error Handling

If the city is not provided, the API will return:

```json
{
  "error": "Please provide a city name"
}
```

If there is an error fetching data from the Weatherbit API, the API will return:

```json
{
  "error": "Failed to fetch data from Weatherbit API"
}
```


### Acknowledgments

- This project uses the [Weatherbit API](https://www.weatherbit.io/api) to fetch weather data.
