## Tutorial:
## https://www.youtube.com/watch?v=Li0Abz-KT78&list=RDCMUCFB0dxMudkws1q8w5NJEAmw&start_radio=1&rv=Li0Abz-KT78&t=275

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
