# from app import root
from models import db, Set

###################

db.drop_all()
db.create_all()