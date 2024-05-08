import requests
from twilio.rest import Client

url = "https://api.weatherapi.com/v1/forecast.json"
params = {"key": "YOUR API KEY", "q": "Amman"}

twilio_sid = "YOUR API KEY"
twilio_auth_token = "YOUR API KEY"

response = requests.get(url, params=params)
weather_data = response.json()

weather_each_day = weather_data["forecast"]["forecastday"]

weather_too_hot = False
for day in weather_each_day:
    for hour in day["hour"]:
        time = hour["time"].split(" ")[1]
        condition = hour["condition"]["text"]
        temp_c = float(hour["temp_c"])

        if temp_c >= 35.0:
            client = Client(twilio_sid, twilio_auth_token)
            message = client.messages.create(
                body=f"Too hot in {day["date"]} at {time}, the temperature is {temp_c}",
                from_="Your Twilio Number",
                to="Your Destination Number"
            )
            print(message.status)
