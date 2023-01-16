import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = '@2019!secret?environment56'
SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://" + os.getenv('DB_USER') + ":"
                           + os.getenv('DB_PASSWORD') + "@"
                           + os.getenv('DB_HOST')
                           + ":3306/essivi_db")

# connect-string: mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

SQLALCHEMY_TRACK_MODIFICATIONS = False
