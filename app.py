#https://github.com/erm/asgi-examples
#https://github.com/pgjones/quart/blob/master/docs/deployment.rst

import os
import sys
from flask import Flask, request




app = Flask(__name__)
app.secret_key = os.urandom(13)





@app.route('/', methods=['GET'])
def Index():
    return 'test'
  




if __name__ == '__main__':
    app.run()
