from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

condition_association_table = db.Table("condiiton_association", db.Model.metadata,
                                       db.Column("condition_id", db.Integer, db.ForeignKey("courses.id")),
                                       db.Column("patient_id"), db.Integer, db.ForeignKey("patients.id"))


class User(db.Model):
  """
  User Model
  """
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)

  def __init__(self, **kwargs):
    """
    Initialize a user object
    """
    self.username = kwargs.get("username")
    self.password = kwargs.get("password")
    self.email = kwargs.get("email")

  def serialize(self):
    """
    Serialize a user object
    """
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email
    }
  
class Patient(db.Model):
  """
  Patient Model (Child)
  """
  __tablename__ = "patients"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  fname = db.Column(db.String, nullable=False)
  lname = db.Column(db.String, nullable=False)
  birthdate = db.Column(db.Date)
  sex = db.Column(db.String, nullable=False)
  guardian_id = db.Column(db.Integer, nullable=False)

  registered_diseases = db.relationship("Conditions", cascade="delete")

  def __init__(self, **kwargs):
    """
    Initialize a patient object
    """
    self.fname = kwargs.get("fname")
    self.lname = kwargs.get("lname")
    self.birthdate = kwargs.get("birthdate")
    self.sex = kwargs.get("sex")
    self.guardian_id = kwargs.get("guardian_id")

  def serialize(self):
    """
    Serialize a patient object
    """
    return {
      "id": self.id,
      "user_id": self.user_id,
      "fname": self.fname,
      "lname": self.lname,
      "birthdate": self.birthdate,
      "sex": self.sex,
      "guardian_id": self.guardian_id,
      "registered_conditions": Conditions.query.filter_by()
    }
  
class Guardian(db.Model):
  """
  Guardian Model (Parent or Legal Guardian of Patient)
  """
  __tablename__="guardians"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  fname = db.Column(db.String, nullable=False)
  lname = db.Column(db.String, nullable=False)
  number = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)

  user_id = db.Column(db.ForeignKey("users.id"))
  password = db.Column(db.ForeignKey("users.password"))
  username = db.Column(db.ForeignKey("users.username"))
  email = db.Column(db.ForeignKey("users.email"))

  # Ensures that the patient (child) is dependent on the legal guardian's account
  # if the guardian is removed from the application, all patients related to that
  # guardian are likewise removed from the application
  dependents = db.relationship("Patient", cascade="delete")

  def __init__(self, **kwargs):
    """
    Initialize a guardian object
    """
    self.fname = kwargs.get("fname")
    self.lname = kwargs.get("lname")
    self.number = kwargs.get("number")
    self.email = kwargs.get("email")
    self.username = kwargs.get("username")

  def serialize(self):
    """
    Serialize a guardian object
    """
    return {
      "id": self.id,
      "fname": self.fname,
      "lname": self.lname,
      "email": self.email,
      "number": self.number,
      "username": self.username
    }
    
class Conditions(db.Model):
  """
  Conditions Model
  """
  __tablename__ = "conditions"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)

  def returnName(self):
    """
    Returns the name of a given condition
    """
    return {
      "name": self.name
    }


  