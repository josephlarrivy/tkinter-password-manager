from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from tkinter import *
import psycopg2

bcrypt = Bcrypt()

db = SQLAlchemy()
def connect_db(root):
    db.root = root
    db.init_app(root)

# try:
#     db = psycopg2.connect(
#     database="Password-Manager", user="postgres", password="dhqiuhwd9189hd29", host="localhost")
#     print("connected")
# except:
#     print("I am unable to connect to the database")
# cur = db.cursor()
# cur.execute(
#     "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# print(coins)
# db.commit()
# cur.close()
# db.close()


#######################

class Set(db.Model):
    __tablename__ = 'sets'

    nickname = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    url = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.String, nullable=False)
    pwd_first_two_characters = db.Column(db.String)
    pwd_last_two_characters = db.Column(db.String)


    @classmethod
    def save_to_db(cls, nickname, url, email, username, password, pwd_first_two_characters, pwd_last_two_characters):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')

        pwd_first_two_characters = password[:2]
        pwd_last_two_characters = password[-2]

        return cls(nickname=nickname, url=url, email=email, username=username, password=hashed_utf8, pwd_first_two_characters=pwd_first_two_characters, pwd_last_two_characters=pwd_last_two_characters)

    @classmethod
    def authenticate(cls, nickname, password):
        s = Set.query.filter_by(nickname=nickname).first()
        if s and bcrypt.check_password_hash(s.password, password):
            return s
        else:
            return False
