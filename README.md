# Instructions

requirements.txt includes the list of dependencies, to install them you can run the command:

    pip -r requirements.txt

Before executing the code in hotels.py, you need to set the FLASK_APP environment variable with the command:

For windows:

    $env:FLASK_APP = "hotels"

For bash:

    export FLASK_APP=hotels

Afterwards, you can start the flask app with the command:

    python -m  flask run

This will start serving the REST api on localhost and you should be able to query endpoints like `http://127.0.0.1:5000/hotels?stars=5`

To run the unit test suite run the following command:

    python test.py
    
