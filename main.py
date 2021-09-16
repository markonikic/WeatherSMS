import requests
from twilio.rest import Client
from data import phoneNumber, api_key, account_sid, auth_token

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = api_key
account_sid = account_sid
auth_token = auth_token

weather_params = {
    "lat": -35.736141,
    "lon": 137.589783,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today! Remember to bring an umbrella!☂️",
        from_="+14153606681",
        to=phoneNumber
    )
    print(message.status)