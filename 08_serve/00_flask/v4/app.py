'''
Shy : Sasha S, Henry B, Yuki F
SoftDev
Oct 2022
DISCO :
    Debugger works
    Recognizes when you change the code
    Interpreted as HTML 
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<h1>No hablo queso!</h1>5tulk"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
