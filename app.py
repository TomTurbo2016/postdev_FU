
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask




app = Flask(__name__)
app.secret_key = os.urandom(13)





@app.route('/', methods=['GET'])
def Index():
    return ("<h1>Hello, World!</h1>")


 

if __name__ == '__main__':
    app.run()
