from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def root():
   now = datetime.now()
   formatted_now = now.strftime("%A, %d %B, %Y at %X")
   return("Hello, " + formatted_now + ".")

@app.route('/<path>')
def home(path):
   if "name" in path:
      return('"name" is in path')
   else:
      now = datetime.now()
      formatted_now = now.strftime("%A, %d %B, %Y at %X")
      return("Hello, " + formatted_now + ", " + path)

if __name__ == "__main__":
    app.run(debug=True)
