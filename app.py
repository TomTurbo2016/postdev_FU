#https://github.com/erm/asgi-examples
#https://github.com/pgjones/quart/blob/master/docs/deployment.rst

import os
import sys
from flask import Flask
import requests




app = Flask(__name__)
app.secret_key = os.urandom(13)





@app.route('/', methods=['GET'])
def Index():
    return ("<h1>Hello, World!</h1>")
  




if __name__ == '__main__':
    app.run()
