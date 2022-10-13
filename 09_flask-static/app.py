'''
Shy: Sasha, Henry, Yuki
SoftDev
11 Oct 2022

DEMO 
basics of /static folder

DISCO:
- when running http://localhost:5000/static/foo, the browser prompts you to 
download the file foo. 
- when running http://localhost:5000/static/foo.html, you get brought to 
a site that prints the text in the body: "Is this plaintext, though?" as opposed to 
"No hablo queso" when running app.py.
- when u run app.py, it prints to the terminal:
    the __name__ of this module is...
    __main__

QCC:
- then what...?
'''

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
