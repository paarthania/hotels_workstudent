from flask import Flask
from flask import request
from markupsafe import escape
import json
from tinydb import TinyDB, Query

# Initialize a simple empty database to simulate real life database that we can query 
db = TinyDB('./empty.json')
db.drop_tables()

with open('./db.json', 'r') as file:
    data = json.load(file)

# Fill the database, with small modification on entries to make them suitable for expected output
for location in data:
    destination = location.capitalize()
    for hotel in data[location]:
        hotel["destination"] = destination
        db.insert(hotel)

app = Flask(__name__)


@app.route("/hotels")
def hotels():
    stars = None
    if "stars" in request.args:
        stars = escape(request.args.get('stars', ''))

    # No stars value provided, return all hotels
    if(stars is None):
        return json.dumps(db.all())

    try:
        stars = int(stars)
    except:
        return "Stars should be valid integer"

    if(stars not in range(1, 6)):
        return "Stars should be between 1 and 5"

    query = Query()
    return json.dumps(db.search(query.stars == stars))
