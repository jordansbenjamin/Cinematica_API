from flask import Blueprint
from main import db, bcrypt
from models.user import User
from models.movie import Movie
from models.watchlist import Watchlist
from models.movielog import MovieLog

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

    # Add all user instances to the DB
    db.session.add_all(users)
    # NOTE: Its basically the same thing as this:
    # for user in users:
    #     db.session.add(user)

    # Commit changes to DB in order for watchlist and movielog to be added to the user
    db.session.commit()

    # List comprehension to create watchlist instance of each user
    watchlists = [
        Watchlist(user_id=user.id) for user in users
    ]

    # Add all watchlist instances to the DB
    db.session.add_all(watchlists)

    # List comprehension to create movielog instance of each user
    movielogs = [MovieLog(user_id=user.id) for user in users]

    # Add all movielogs instances to the DB
    db.session.add_all(movielogs)

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
        Movie(
            title='Oppenheimer',
            director='Christopher Nolan',
            genre='Drama/Thriller',
            runtime='180 min',
            release_year=2023,
        ),
        Movie(
            title='Barbie',
            director='Greta Gerwig',
            genre='Comedy/Drama',
            runtime='114 min',
            release_year=2023,
        ),
        Movie(
            title='The Apartment',
            director='Billy Wilder',
            genre='Rom-Com',
            runtime='125 min',
            release_year=1960,
        ),
    ]

    # Add all movie instances to DB
    db.session.add_all(movies)
    # Commit to DB
    db.session.commit()

    print("DB Tables seeded!")
