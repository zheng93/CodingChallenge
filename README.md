# Pre-requsites:
> The project is developed in Python. Please install Python 3.8 and above on your machine.
>
> Please also make sure pip package installer is also installed.

# How to install and use:
1. Change the execution permission for installer.sh
> chmod +x installer.sh
> 
2. Run the bash script that installs required python packages
> sh installer.sh
> 
3. Start the web server/api
> python api.py
> 
or 

> python3 api.py


4. While our web server/api is running, you can send HTTP get request to our api. The server runs at http://127.0.0.1:5000. Port 5000 is the default port used here.

An example of an api request goes like this:
> "GET http://127.0.0.1:5000/locations?location=ASZE HTTP/1.1"
> 

If the provided location key is valid in the request, a sample response will be like this:
> {"Key": "ASZE", "Temperature": "51 F (11 C)", "Pressure": "30.15 in. Hg (1021 hPa)"}

which contains the location key, temperature and pressure data.

If the provided location key is not valid, user will get a message saying:
> "Invalid location key! Bad request!"

# Test
A test file named Test.py includes some unit tests that verifies that our api is working and returning correct data. Simply run the Test.py file and the unit tests will be run.
