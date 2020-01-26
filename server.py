from flask import request
from flask_api import FlaskAPI

import polit
# from chainbase import contract_address

app = FlaskAPI(__name__)

get = ['GET']
post = ['POST']


@app.route("/", methods=get+post)
def country_list():
    """
    List of country options available, currently hard-coded
    TODO: Extend
    """
    try:
        return polit.regions
    except:
        return "Record not found", 400


@app.route("/elections", methods=get)
def province_list():
    """
    Returns a list of supported provincial elections where API
    can be applied, currently restricted by hard-coding.
    TODO: Extend
    """
    country = request.args.get("country")
    try:
        return {country: polit.regions[country]}
    except:
        return "Record not found", 400

@app.route("/candidates", methods=get)
def candidate_list():
    """
    Returns a list of supported provincial elections where API
    can be applied, currently restricted by hard-coding.
    TODO: Extend
    """
    country = request.args.get("country")
    election = request.args.get("election")
    try:
        temp = "%s/%s" % (country, election)
        return {temp : polit.regions[country][election]}
    except:
        return "Record not found", 400

if __name__ == '__main__':
    app.run(debug=True)
