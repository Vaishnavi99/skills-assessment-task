from flask import Flask, Response
import pandas as pd
import re, datetime, requests

app = Flask('PresidentialDataServerA')
def getAcronyms(txt):
    words =  re.split(r'[-,\s]\s*', txt)
    return "".join([word[0] for word in words])

@app.route('/', methods=['GET'])
def home():
    return '''<p>API for presidential data: http://127.0.0.1:5001/api/data/presidents</p>'''

@app.route('/api/fetch/presidentialdata', methods=['GET'])
def presidentData():
    r = requests.get('http://127.0.0.1:5001/api/data/presidents')
    return Response(
    r.text,
    mimetype="text/csv",
    headers={"Content-disposition":
             "attachment; filename=presidentialdata.csv"})

@app.errorhandler(404)
def page_not_found(e):
    return "<center><h1>404</h1><p>The resource could not be found.</p></center>", 404
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

