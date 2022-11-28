'''
TPNG: JoY
ROSTER: Yuki Feng, Joshua Liu
DISCO:
    requests module can be used to send get requests.
    .json() can be used to parse the request object into a json dictionary.
QCC:
    image is cool.
Time Spent: 1.5
'''

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    key = "DEMO_KEY"
    with open("key_nasa.txt") as file:
        key = file.read()
        #print("KEY: " + key)
    url = "https://api.nasa.gov/planetary/apod?api_key=" + key
    #print("URL : " + url)
    data = requests.get(url).json()
    image_url = data["url"]
    ex = data["explanation"]
    return render_template("main.html", image=image_url, explanation=ex)

if __name__ == "__main__":
    app.debug = True
    app.run()
