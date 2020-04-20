import json

from flask import Flask, render_template

from packages.measurement_levels import MeasurementLevels

# setup minimal flask app
app = Flask(__name__)

# retrieve measurement stations
with open("measurement_stations.json", "r") as fp:
    measurement_stations = json.load(fp)


# define app routes
@app.route("/", methods=['GET', 'POST'])
def welcome():

    msg = """
    Hi, falls du nach den Pegelständen in und um Passau suchst, versuch es mal mit folgender URL:
    http://localhost:5000/water_levels
    """
    return msg

# define app routes
@app.route("/water_levels", methods=['GET', 'POST'])
def measurement_levels():

    # retrieve latest measurements
    current_measurements = MeasurementLevels.fetch_all_stations(measurement_stations)

    return render_template('index.html', cm=current_measurements)

if __name__ == "__main__":
    app.run()