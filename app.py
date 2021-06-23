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
    body = request.get_data()
    user = 'christian.hahna@post.at'
    password = 'AIIn ZFXk xh8V r8vx'
    wsdl_url = 'https://at.cloud.fabasoft.com/folio/fscdav/wsdl?WEBSVC=POSTMSPORTAL_111_100_CustomerPortalWebService'
    headers={'content-type': 'text/xml'}
    response = requests.post(url=wsdl_url,data=body,headers=headers,auth=(user,password),verify=False,timeout=(5.0, 5.0))
    return (str(response.content.decode("utf-8")))

 

if __name__ == '__main__':
    app.run()
