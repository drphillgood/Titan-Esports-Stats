#### README FILE FOR TITAN ESPORTS GAME STATS (LEAGUE OF LEGENDS) ####

## LIST OF FILES ##

- **run.sh** - This is the main file to run in shell. The user must pass 2 arguments when running this file (the week and name of league). For example: ```./run.sh wk1 Divinity```
- **scripts/codes.js** - This is where tournament codes will be placed. File contains valid tournament codes from Spring 2021 Invitational to utilize (need to be uncommented)
- **scripts/credentials.json** - Credentials for using Google's oauth to upload documents to Google Sheets. These variables will need to be supplied by the user: ```client_id, project_id, client_secret```. 


## OTHER REQUIREMENTS ##
The following are required to run this script.

- [Node.js](https://nodejs.org/en/)
  - [Google API Client](https://pypi.org/project/google-api-python-client/)
- [Python 3](https://www.python.org/downloads/)
  - [PIP](https://pip.pypa.io/en/stable/reference/pip_install/) 
