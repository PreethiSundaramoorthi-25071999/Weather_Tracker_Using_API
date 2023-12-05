from flask import Flask,render_template,request

import requests

app = Flask(__name__)

api_key = '4876232ef40a55b6706094bcc5cb76c9'

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/weather', methods = ["GET","POST"])
def home():
    if request.method == "POST":
        City = request.form.get("City")
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&APPID={api_key}")
        data=weather_data.json()
        return render_template ("home.html",temp=data.get("main").get("temp"),pressure=data.get("main").get("pressure"),feels=data.get("main").get("feels_like"),humidity=data.get('main').get("humidity"),wind=data.get("wind").get("speed"),name=data.get("name"),sunrise=data.get("sys").get("sunrise"),sunset=data.get("sys").get("sunset"),clouds=data.get("weather")[0].get("description"))
    return render_template ("home.html")

if __name__ == "__main__":
    app.run(debug=True)





# (f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={api_key}")



























