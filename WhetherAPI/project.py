from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Send a GET request to /weather with 'city' as a query parameter to get weather data."

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    api_key = "e56f5d60c8614ce8bb4bc832c64b822f"
    url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  

        
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content.decode('utf-8')}")

        data = response.json()
        return jsonify(data)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  
        return jsonify({"error": "Failed to fetch data from Weatherbit API"}), response.status_code
    except Exception as err:
        print(f"Other error occurred: {err}")  
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
