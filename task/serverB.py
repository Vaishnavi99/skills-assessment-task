from flask import Flask, Response
import pandas as pd
import re, datetime

app = Flask('PresidentialDataServerB')
def getAcronyms(txt):
    words =  re.split(r'[-,\s]\s*', txt)
    return "".join([word[0] for word in words])

@app.route('/', methods=['GET'])
def home():
    return '''<p>API for presidential data: http://127.0.0.1:5001/api/data/presidents</p>'''
 
@app.route('/api/data/presidents', methods=['GET'])
def presidentData():
    df = pd.read_json('data/presidentData.json').drop("id", axis=1)
    df['Ingestion Time'] = datetime.datetime.now()
    # add century column to dataframe
    df['century'] = df['tm'].apply( lambda x: int(x.split('-')[0]) // 100 + 1)
    
    # remove any president from the Federalist party
    df = df[df['pp'].str.find("Federalist") < 0]
    
    # first names and they should be backwards
    df['nm'] = df['nm'].apply(lambda x: x.split(' ')[0][::-1])
    df = df.sort_values('nm')
    
    df['pp'] = df['pp'].apply(getAcronyms)
    df['tm'] = df['tm'].apply(lambda x: "mm-dd-" + x.split('-')[0])
    
    df.rename(columns={'nm': 'Name', 'pp': 'Party', 'tm': 'Presidential Term', 'president': 'President Number'}, inplace=True)
    final_df = df[['Name', 'Party', 'Presidential Term', 'President Number', 'Ingestion Time' ]]
    
    csv = final_df.to_csv(index=False, header=True)
    return Response(
    csv,
    mimetype="text/csv",
    headers={"Content-disposition":
             "attachment; filename=presidentialdata.csv"})

@app.errorhandler(404)
def page_not_found(e):
    return "<center><h1>404</h1><p>The resource could not be found.</p></center>", 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)

