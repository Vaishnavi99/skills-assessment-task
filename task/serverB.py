from flask import Flask, Response
import pandas as pd
import re, datetime

app = Flask('PresidentialDataServerB')
def getAcronyms(txt):
    words =  re.split(r'[-,\s]\s*', txt)
    return "".join([word[0] for word in words])
 
@app.route('/api/data/presidents', methods=['GET'])
def presidentData():
    df = pd.read_json('data/presidentData.json').drop("id", axis=1)
    df['Ingestion Time'] = datetime.datetime.now()
    
    # add century column to dataframe
    df['century'] = df['tm'].apply( lambda x: int(x.split('-')[0]) // 100 + 1)
    df = df.sort_values('century')

    # remove any president from the Federalist party
    df = df[df['pp'].str.find("Federalist") < 0]
    
    # first names spelled backwards
    df['nm'] = df['nm'].apply(lambda x: x.split(' ')[0][::-1])
    
    # Sort President's name alphabetically
    df = df.sort_values('nm')
    
    # store the name of party as acronyms
    df['pp'] = df['pp'].apply(getAcronyms)
    
    # include the year the president began their term in
    df['tm'] = df['tm'].apply(lambda x: "mm-dd-" + x.split('-')[0])
    
    # Update columns names as required in the final output
    df.rename(columns={'nm': 'Name', 'pp': 'Party', 'tm': 'Presidential Term', 'president': 'President Number'}, inplace=True)
    # select the required columns and store in a dataframe
    final_df = df[['Name', 'Party', 'Presidential Term', 'President Number', 'Ingestion Time' ]]
    # convert the data in dataframe to a csv format
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

