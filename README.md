# CS551Q-Assessment
#### Codio Terminal Commands
##### Startup Commands
source .venv/bin/activate 	# this activates the virtual environment
python3 manage.py runserver 0.0.0.0:2500 #  the app locally  on port 2500, shown in the URL below

https://plazajason-telexvelvet-2500.codio-box.uk/
(This will change depending on the codio box it is run in)

##### GitHub  Commands
- git status              #check the current status of the GitHub repository
- git add .               #add changes to the local repo
- git commit -m "update"  #save changes made to the local repo
- git push origin master  #push the local changes to the master branch of the repo

These commands are used to update the Git server and check the status 
GitHub Username: Xenterra
GitHub Repository Name: CS551Q_Assessment

##### Heroku Commands
- git push heroku master   #commit the changes of Git's master branch to Heroku, this will redeploy as a new version
- heroku status         #used to check how the Heroku deployment is progressing

Heroku URL: https://secret-plateau-57057.herokuapp.com/

As heroku is run automatically, use the status command to check its functioning well, and the 'git push' command to apply changes to a new version of the app

##### Pages:
- /          # Home page that can display all the data, app also starts here
- /compare   # This page allows the user to compare two universities using their ID numbers
- /search    # Page that allows the User to search throught he data to find what they need
- /selected  # This page follows on from either the home or the search page to allow a user to see all the details from one entry

##### Testing
There is no automated testing present in this project due to time restraints 

An aid in testing has been provided in the form of commented 'print()' functions that can be used to display values throughout the code
Use these to check that the correct values are beeing passed at different points in the program's use.

#### Remaining Errors:
- (minor) 
- (major) The search feature only accepts responses that are accurately spelt and formatted
-- i.e. University of Aberdeen will not appear when searching "Aberdeen" or "university of aberdeen"