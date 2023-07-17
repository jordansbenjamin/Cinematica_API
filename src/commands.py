from flask import Blueprint
from main import db, bcrypt

# Initialises flask blueprint for DB CLI commands
db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    '''Initialises DB tables'''
    db.create_all()
    print("DB Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("DB Tables dropped!")

