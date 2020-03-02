# Skills-assessment-task

## Setup the environment
### Use the following two commands to setup and activate a virtual environment in python
`python3 -m venv venv` //create a virtual environment <br/>
`source venv/bin/activate` // activate the virtual environment

### Installing  the dependencies:
Run the following command to install all dependencies once the environment is setup. <br/>
`pip3 install -r requirements.txt`


## Executing the code
All files reside in the **task** directory. Chnage current directory to the task directory in order to run flask servers:<br/>
`cd task `

We setup and run two flask servers:<br/>
**Server A:** server that pings server B to get manipulated Presidential Data<br/>
**Server B:** server that hosts an app which ingests data from json file(in the data directory),  manipulates it as required and returns the response as a CSV file<br/>

Make sure you are in the task directory<br/>
### To run flask server A: (Runs on port: 5000)
`python3 serverA.py`

Open a new terminal window.
### To run flask server B:  (Runs on port: 5001)
`python3 serverB.py`

Once both servers are up and running ping ServerA using http://127.0.0.1:5000/api/fetch/presidentialdata to download the desired CSV file contaning manipulated presidential data.


## Approach
JsonFile containing President data is stored in the task/data directory. The app running on server B does the following tasks to manipulate the data:<br/>
* Load data from the json file in data directory to a pandas dataframe and drops the 'id' column.
* Data Ingestion column is added to dataframe with current timestamp. [No format specified for timestamp]
* Add a century column to the dataframe [**Assumption:** It is not very clear what to do after dividing the data by century of the president's term, so the dataframe is sorted by 'century' column in order to make sure presidents with terms belonging to one century are grouped together. Also, the starting year of the president's term is used to calculate century as no information is given as to how to accurately calculate the century of year a president was in power]
* Remove any presidents from the Federalist party.
* Updates President's names to include their first names spelled backwards.
* Sorts the data by President's name alphabetically[**Assumption:** Since, no information is given whether to sort the Presidents list by their actual names given in the json file or their updated names(first names spelled backwards), the data in this assignment is sorted by the updated presidents names(irst names spelled backwards)]
* Updates the name of the party as and stores them as acronyms.
* Updates the president's term column to only include the year the president began their term in. [**Assumption:** Data is stored in the format mm-dd-yyyy for example: mm-dd-2017]
* The columns in dataframe are renamed to the desired headers as mentioned in the assessment doc.
* The required columns are selected as a final dataframe.
* The data in dataframe is converted to CSV format with headers as required in output.
* The data is then send back as Response in the form of CSV file. This is achieved using a Response object with desired data and headers.

Tasks performed by Server A: <br/>
* It pings server B to get all the presidential data. Once the file is received from Server B, server A responds with a CSV file, having the data as returned by server B. File named 'presidentialdata.csv' is downloaded automatically once the request from server B is completed successfully.


## Improvements
* Instead of sending csv file from server B, manipulated data can be sent back as text in a csv format and then server A can be used to send the csv formatted data back to user as a CSV file.
* Include API authentication in order to establish a secure connection.




