# ---- Flask Hello World ----# 

# import the Flask class from the flask package 
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to 
# link the view function to a url
@app.route("/")
@app.route("/hello")

# devind the view using a function, which returns a string
def hello_world():
    return "Hello,World! I WILL CREATE HISTORY. I WILL SELL MY AI PRODUCT FOR USD120mn to Microsoft "

#  start the development server using the run() method 
if __name__ == "main()":
    app.run(debug = True, port = 5000)



