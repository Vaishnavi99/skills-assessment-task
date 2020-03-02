# skills-assessment-task

## Setup the environment
---

### Use the following two commands to setup and activate a virtual environment in python
`python3 -m venv venv //create a virtual environment
source venv/bin/activate // activate the virtual environment`

### Install the dependencies by running the following command once the environment is setup:
`pip3 install -r requirements.txt`


## Executing the code
--- 
All files reside in the **task** directory. Chnage current directory to the task directory in order to run flask servers:
`cd task `

We setup and run two flask servers:
**Server A:** server that pings server B to get manipulated Presidential Data
**Server B:** server that hosts an app which ingests data from json file(in the data directory),  manipulates it as required and returns the response as a CSV file

### To run flask server A: 
`python3 serverA.py`

Open a new terminal window.
### To run flask server B:
`python3 serverA.py`

Once both servers are up and running ping ServerA using http://127.0.0.1:5000/api/fetch/presidentialdata to get the desired CSV file contaning manipulated presidential data.


