import json
from flask import request
from db import db
from db import User, Patient
from flask import Flask

app = Flask(__name__)
db_filename = "database.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()


# Generalized responses for requests
def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({"error": message}), code

# API Routes:
@app.route("/user/<int: patient_id>") # GET: Get information about a specific patient
def get_user(patient_id):
    """
    Endpoint that returns the serialization of a specified user object
    """
    patient = Patient.query.filter_by(id=patient_id).first()
    if patient is None:
        return failure_response("Patient not found!")
    return success_response(patient.serialize())

@app.route("/user/") # POST: Create a user object
def create_user():
    """
    Endpoint that creates a new user object
    """
    body = json.loads(request.data)
    username = body.get("username")
    if username is None:
        failure_response("You did not enter a username", 400)

    password = body.get("password")
    if password is None:
        failure_response("You did not enter a password", 400)

    fname = body.get("first name")
    if fname is None:
        failure_response("You did not enter a first (given) name", 400)

    lname = body.get("last name")
    if lname is None:
        failure_response("You did not enter a last (family) name", 400)

    email = body.get("email")
    if email is None:
        failure_response("You did not enter an email", 400)

    birthdate = body.get("birthdate")
    if birthdate is None:
        failure_response("You did not enter a birthdate", 400)

    sex = body.get("sex")
    if sex is None:
        failure_response("You did not enter a sex", 400)

    patient = Patient(
        username=username,
        password=password,
        email=email,
        fname=fname,
        lname=lname,
        birthdate=birthdate,
        sex=sex
    ) 

    db.session.add(patient)
    db.session.commit()
    return success_response(patient.serialize(), 201)