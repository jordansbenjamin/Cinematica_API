from flask import Blueprint
from main import db, bcrypt

# Initialises flask blueprint for DB CLI commands
db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    '''This command will initialise DB tables'''
    db.create_all()
    print("DB Tables created!")