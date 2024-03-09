from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
db_filename = "database.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True