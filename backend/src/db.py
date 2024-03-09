from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

  user_id = db.Column(db.ForeignKey("users.id"))
  username = db.Column(db.ForeignKey("users.username"))
  email = db.Column(db.ForeignKey("users.email"))

  def __init__(self, **kwargs):
    """
    Initialize a patient object
    """
    self.username = kwargs.get("username")
    self.password = kwargs.get("password")
    self.email = kwargs.get("email")
    self.fname = kwargs.get("fname")
    self.lname = kwargs.get("lname")
    self.birthdate = kwargs.get("birthdate")
    self.sex = kwargs.get("sex")

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
      "sex": self.sex
    }