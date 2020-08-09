# adapted from the programminghistorian.org
import flask
from flask import request, jsonify
from werkzeug.utils import redirect

from algorithm import determine_risk_level

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
risk_levels = [
    {'id': 0,
     'risk_level' : 'HIGH'},
    {'id': 1,
     'risk_level' : 'MEDIUM'},
    {'id': 2,
     'risk_level' : 'LOW'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Risk Level</h1>
<p>An evaluation of your risk level based off of the survey'''


@app.route('/api/v1/routes/levels/all', methods=['GET'])
def api_all():
    return jsonify(risk_levels)


@app.route('/api/v1/resources/levels', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    '''
    if risk_levels[id]['id'] == id:
        results.append(risk_levels[id]['risk_level'])

    '''

    if risk_levels[id]['id'] == id:
        return "You are at " + risk_levels[id]['risk_level'] + " RISK for COVID"
    '''
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

    '''

''' post request from front end
@app.route('/login/', methods=["POST"])
def export_risk_level():
    error = ''
    if request.method == "POST":

        attempted_username = request.form['username']
        attempted_password = request.form['password']

        url = "http://127.0.0.1:5000/api/v1/resources/levels?id={}".format(determine_risk_level(slider_inputs))
        return redirect(determine_risk_level())

app.run()
'''
