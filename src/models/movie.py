from main import db

class Movie(db.Model):
    # Table name for db
    __tablename__ = 'movies'

    # Sets the movies PK
    id = db.Column(db.Integer(), primary_key=True)
    # Movie's title
    title = db.Column(db.String(128), nullable=False)
    # Movie's director
    director = db.Column(db.String(64), nullable=False)
    # Movie's genre
    genre = db.Column(db.String(32), nullable=False)
    # Movie's runtime
    runtime = db.Column(db.String(16), nullable=False)
    # Movie's release date
    release_year = db.Column(db.Integer(), nullable=False)

    # Establishing relationships:
    # WILL DO AFTER OTHER MODEL ARE CREATED FIRST