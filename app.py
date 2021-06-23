from flask import Flask, request
import os, sys
import requests
from requests.auth import HTTPBasicAuth




app = Flask(__name__)
app.secret_key = os.urandom(13)





@app.route('/', methods=['GET'])
def Index():
    return ("<h1>Hello, World!</h1>")

@app.route('/200', methods=['POST'])
def Index2():
    return ("hallo123")

 

if __name__ == '__main__':
    app.run()
