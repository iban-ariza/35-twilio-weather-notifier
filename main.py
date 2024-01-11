import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = os.environ.get("OWM_API_KEY")
account_sid = ""
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# to_number = os.environ.get("TWILIO_TO_NUMBER")
api_key = ""
auth_token = ""
to_number = ""

# change for lat, lon where there is rain to see the results
weather_params = {
    "lat": 32.776566,
    "lon": -79.930923,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18558283764",
        to=""
    )
    print(message.status)
    # Toll free numbers (ones created by Twilio) must be verified (given business address, name, ...)
    # otherwise the messages will be queued (message.status==queued) and won't be delivered.

