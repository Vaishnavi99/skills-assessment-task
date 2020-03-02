from flask import Flask, Response
import pandas as pd
import requests

app = Flask('PresidentialDataServerA')

@app.route('/')
def home():
    return '''<p>Server A: Try pinging http://127.0.0.1:5000/api/fetch/presidentialdata to fetch all Presidential data.</p>'''

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

