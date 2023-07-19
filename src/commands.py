from flask import Blueprint
from main import db, bcrypt
from models.user import User
from models.movie import Movie
from models.watchlist import Watchlist

# Initialises flask blueprint for DB CLI commands
db_commands = Blueprint('db', __name__)


@db_commands.cli.command("create")
def create_db():
    '''Initialises DB tables'''
    db.create_all()
    print("DB Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    '''Drops/removes DB tables'''
    db.drop_all()
    print("DB Tables dropped!")


@db_commands.cli.command("seed")
def seed_db():
    '''Seeds DB with test data'''
    # Creates user instances within a list instead of separating each instance and having to add each instance everytime
    users = [
        User(
            email='user1@mail.com',
            username='user1',
            password=bcrypt.generate_password_hash('user1pw').decode('utf-8')
        ),
        User(
            email='user2@mail.com',
            username='user2',
            password=bcrypt.generate_password_hash('user2pw').decode('utf-8')
        ),
    ]

    # db.session.add_all(users)
    # TESTING: 
    for user in users:
        db.session.add(user)

    db.session.commit()

    watchlists = [
        Watchlist(user_id=user.id) for user in users
    ]

    db.session.add_all(watchlists)

    # Creates movie instances within a list instead of separating each instance and having to add each instance everytime
    movies = [
        Movie(
            title='Inception',
            director='Christopher Nolan',
            genre='Drama/Sci-Fi',
            runtime='148 min',
            release_year=2010,
        ),
        Movie(
            title='Spiderman',
            director='Sam Raimi',
            genre='Superhero',
            runtime='121 min',
            release_year=2002,
        ),
        Movie(
            title='Psycho',
            director='Alfred Hithcock',
            genre='Horror/Thriller',
            runtime='109 min',
            release_year=1960,
        ),
        Movie(
            title='Jaws',
            director='Steven Spielberg',
            genre='Adventure/Thriller',
            runtime='124 min',
            release_year=1975,
        ),
    ]

    db.session.add_all(movies)

    db.session.commit()

    print("DB Tables seeded!")
