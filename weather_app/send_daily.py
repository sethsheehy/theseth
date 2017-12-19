import json
import os
import urllib2
from sendgrid.helpers.mail import *
from sendgrid import *

def get_weather_city(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}"
    data = requests.get(url.format(city_name))
    return data

def send_daily_weather(city_name, to_addr):
    # get weather data
    data = get_weather_city(city_name)

    # send weather data
    mail = Mail()

    mail.from_email = Email("reminder@daily-weather.com", "Today's Weather")
    mail.subject = "Today's Weather for " + city_name

    mail.template_id = "20j8v91b-plve-ee46-h1j9-60fbc9ow2194"

    personalization = Personalization()
    personalization.add_to(to_addr)
    personalization.add_substitution("%city_name%", city_name)

    personalization.add_substitution("%temp%", temp)
    personalization.add_substitution("%condition%", condition)
    personalization.add_substitution("%condition_description%", condition_description)

    mail.add_personalization(personalization)

    sg = SendGridAPIClient(apikey=os.environ.get('SG_KEY'))

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.headers)
        print(response.body)
    except:
        Exception("SendGrid send failed - please check API usage.")
