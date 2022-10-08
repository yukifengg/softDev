'''
Shy : Sasha S, Henry B, Yuki F
SoftDev
Oct 2022
Time spent: 1.0 hr

DISCO:
    - The return type must be a string, dict, list, tuple with headers or status,
    Response instance, or WSGI callable, but it was a JpegImageFile
    - you can display an image like you would in html! do so by setting the img src
    like so:
        <img src = '/static/[filename]'>
QCC:
    - our error in trying to import the image in class was an extra ' disrupting
    the code
'''

from flask import Flask
import random as rng
from PIL import Image

app = Flask(__name__)

def readFile() :
    file_text = open("occupations.csv").read()
    jobs = file_text.split("\n")
    new_dict = {}
    for job in jobs[1:-2] : # Look at every job excluding the first line and last lines
        job = job[::-1] # Reverse the string
        (percentage, occupation) = job.split(",", maxsplit=1) # Split the string once, and set percentage and occupation
        percentage = (float)(percentage[::-1]) # Re-reverse percentage and convert it to a float
        occupation = occupation[::-1] # Re-reverse occupation
        if occupation not in list(new_dict) :
            new_dict[occupation] = percentage # Add the job
    return new_dict

def randOccupation() :
    job_dict = data
    occupations = [] #create empty list
    for occupation in list(job_dict) : #iterate
        percentage = job_dict[occupation] #grabs occupation percentage
        for i in range((int)(percentage*10)):
            occupations.append(occupation) #adds occupation based on Percentage
    job = rng.choice(occupations) #random job
    return job #returns said job

data = readFile()

@app.route("/")
def print_to_screen():
    rand_job = (str)(randOccupation())
    job_for_link = rand_job.replace(" ", "-").replace(",", "")
    link = "<a href = https://www.wikipedia.org/w/index.php?search=" + job_for_link + ">" + rand_job + "</a>"
    return (
    "<center><h1>Shy: Sasha, Henry, Yuki</h1>" +
    "<img src='/static/OIP.jpeg'> <h2> List of Occupations: </h2> </center>"
    + str(data) + "<br><br> <b><center> Random Job: " + link + "</center></b>")

if __name__ == "__main__":
    app.debug = True
    app.run()
