from flask import Flask, render
import requests

app = Flask(__name__)

@app.route('/current/<city_name>')
def home(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}"
    general_data = requests.get(url.format(city_name))
    condition = general_data["weather"]["main"]
    condition_description = general_data["weather"]["main"]["description"]
    temp=general_data['main']['temp']
    return render_template('templates/current_city.html', condition=condition,
                                                          condition_description=condition_description,
                                                          temp=temp
                                                          general_data=general_data)

if __name__ == "__main__":

    app.run()
