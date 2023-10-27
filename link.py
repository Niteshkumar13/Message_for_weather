import requests
import twilio.http
import os
from twilio.rest import Client
#first of all you need to login in twilio and openweather to get their key
from twilio.http.http_client import TwilioHttpClient
key = "get api key from openweater"
web = "https://api.openweathermap.org/data/2.5/onecall"
parameter = {
    #find you lat and lon from Latlong.net
    "lat":25.5940,
    "lon":-85.1376,
    "appid":key,
    "exclude":("current,minutely,daily")
}
x = requests.get(web,parameter)
x.raise_for_status()
data = x.json()
weather_day = data["hourly"][:12]

p = False
for i in weather_day:
    condition = i["weather"][0]["id"]

    if condition ==800:
        p = True
#here you need to put your accound_sid and token which you got from twilio
account_sid = "your sid"
auth_token = "your token"
if p:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https':os.environ['https_proxy']}
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hi Nitesh, today seems like hot day',
        #here you put number which is given by twilio
        from_='+13613212339',
        #here you put verify number in which you want message
        to='+916206612349'
    )

    print(message.sid)
