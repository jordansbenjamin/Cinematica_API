# Cinematica API

A RESTful API for movie enthusiasts to review, rate and keep track of movies throughout their cinematic journey.

This project is developed as an assignment for Coder Academy, it being an API webserver, there is no front-end implemented. To test the functionality of the API, you can use API client testing tools such as Postman or Insomnia to have a UI to test the API endpoints on.

---

## Installation Guide

### System Requirements

To start testing the API, since it was developed and built on Python. It is a requirement that **Python 3** is installed on your computer.

You can check which version of python is installed or if you have it installed at all by:

#### Checking version of Python in the Terminal / shell

1. Depending on your operating systems, there are different ways to open the terminal/shell:

- For Macintosh `CMD + space` to open spotlight, then simply type in **_terminal_**
- For Windows `Windows key + x` then select **_command prompt_**. Followed by typing `bash` in the command prompt.

For both operating systems, type:

```shell
python --version
```

If you don't have Python 3 already installed, please follow visit this [_website_](https://realpython.com/installing-python/) for steps on installing Python 3 to your device and operating system of choice.

Please make sure have **Python 3.11+** version installed.

Operating System requirements to run Python:

- Windows 7,10 or 11
- Mac OS X 10.11 or higher, 64-bit
- Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
  - x86 64-bit CPU (Intel / AMD architecture)
  - 4 GB RAM
  - 5 GB free disk space

#### PostgreSQL

Cinematica API's database management system is PostgreSQL, and it is required that PSQL is setup in your device and connecting the database to the Cinematica Flask application in order to test the functionality of the API.

Before continuing with the installlation process, please make sure PostreSQL is installed. You can find and download PostgreSQL for your device and operating system [_here_](https://www.postgresql.org/download/).

### Installation steps

1. Once terminal/shell is open and both Python & PostgreSQL is installed, you can check where you are in the computer directory tree currently by typing in your terminal/shell:

```shell
pwd
```

Next, decide where you want the application folder downloaded (like your Desktop or downloads folder for example) like so:

```shell
cd /Users/username/Desktop
cd /Users/username/Downloads
```

2. After that, you need to clone the [Github Repo](https://github.com/jordansbenjamin/Cinematica_API), simply copy and paste this command to your terminal:

```shell
git clone https://github.com/jordansbenjamin/Cinematica_API.git
```

3. Once its downloaded, you can go to the root directory of the file/project using this command:

```shell
cd Cinematica-API
```

4. After that, type these two commands **_separately_** to allow permission for executing the Blackjack program:

```shell
chmod +x setup_db.sh
```

```shell
chmod +x setup_env_run.sh
```

5. To get you set up before running the Cinematica API program, the PostgreSQL database for the program needs to be set up, thankfully, all you need to do is run the bash script command here:

```shell
./setup_db.sh
```

6. After the database is setup, you need to install some requirements, dependencies, and also setting up the environment variables required to run the program:

```shell
./setup_env_run.sh
```

This bash script will also automatically activate the virutal environment required to run the program but also run the program itself.

7. Lastly, you can test the API itself either through your browser using the localhost URL of `localhost:5000/` or `http://127.0.0.1:5000/` either through your browser or an API client testing tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/).

### Running the program in the future

However, once everything is set up, the bash script is no longer required. All you need to do in the future to run the program is to follow these steps:

1. Go to the **src** folder location, type this command on the terminal:

```shell
cd Cinematica_API/src
```

2. Once you are in the `src` directory, all you need to do to run the program is by typing:

```shell
flask run
```

### CLI DB Commands

The CLI DB commands is required to create the database tables, then seed the tables and also drop the tables. These commands are as follows:

```shell
flask db drop
flask db create
flask db seed
```

When initially setting up the project, these commands are already included in the `./setup_env.run` bash script.

So, if you wish to reset the database when using the API and start fresh, please refer to those commands to type in the terminal/shell before running `flask run`.

### Dependencies

The requirements to start the Cinematica API program have the following dependencies, all automatically installed into the virtual envrionment when you follow the steps above:

```txt
bcrypt==4.0.1
blinker==1.6.2
click==8.1.5
Flask==2.3.2
Flask-Bcrypt==1.0.1
Flask-JWT-Extended==4.5.2
flask-marshmallow==0.15.0
Flask-Psycopg2==1.3
Flask-SQLAlchemy==3.0.5
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
marshmallow==3.19.0
marshmallow-sqlalchemy==0.29.0
packaging==23.1
psycopg2==2.9.6
psycopg2-binary==2.9.6
PyJWT==2.7.0
python-dotenv==1.0.0
SQLAlchemy==2.0.19
typing_extensions==4.7.1
Werkzeug==2.3.6

```

---

## API Documentation

This section covers all the documentation required for each endpoint available in the Cinematica API, with a total of 28 endpoints.

Since this is the first iteration MVP of the Cinematica API, accessing the API would be done through a base local host URL. This can be `localhost:5000/` or the recommendation (more especially for Mac users) would be to use `http://127.0.0.1:5000/` in either an API client testing tool such as Postman or Insomnia, or simply your browser.

### Index

The first endpoint when a user visits and access the Cinematica API would be the `index` endpoint, serving as the main point of entry (homepage) of the API.

**Purpose:** Simply displays a welcome message to the users accessing the API.

**HTTP method:** `GET`

**Endpoint URL:** `/`

**Full route path URL:** `http://127.0.0.1:5000/`

**Arguments:** Not required

**Expected request body:** Not required

**Expected response body:**

```json
{
	"message": "Welcome to Cinematica! A web API for movie enthusiasts to keep track and share their thoughts whilst embarking on their cinematic journey!"
}
```

**Authentication:** Not required

## Auth

The authentication module contains a single endpoint for allowing users to `log in` to the Cinematica API, providing them a JWT access token when successfully logged in to which the token can be used for accessing certain endpoints only users can access.

### Login

**Purpose:** Simply provides a successfully logged in user a JWT token to allow access to other endpoints in the API.

**HTTP method:** `POST`

**Endpoint URL:** `/auth/login`

**Arguments:** Not required

**Full route path URL:** `http://127.0.0.1:5000/auth/login`

**Authentication:** Does not require authentication, it does however, provide the JWT access token required for accessing other endpoints only registered and logged in users are authorised to access.

**Expected request body:**

```json
{
	"username": "user1",
	"password": "user1pw"
}
```

**Expected response body:**

```json
{
	"message": "Successfully logged in!",
	"user": "user1",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTI4MjQxMywianRpIjoiYjBhOWM0Y2EtYzBlZS00MzZiLWIwODMtYzY5OGM0YWE0M2FkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2OTEyODI0MTMsImV4cCI6MTY5MTM2ODgxM30.M44jtWP8E42vmNdGbPBiYfmTRpEAw9GlmV6cBqXF_BQ",
	"expiry": "24 hrs"
}
```

**Expected error response:**

If username or password is incorrect.

```json
{
	"error": "Invalid username and password, please try again"
}
```

## User

The user component of the Cinematica API contains several endpoints that involves fetching information of either all users or a single user available in the Cinematica API. Additionally, endpoints for the creation/registering of the user is available as well as updating a specific users information and lastly deleting the user from the API completely.

### Fetch all users

**Purpose:** Fetches information of all available users in the Cinematica API.

**HTTP method:** `GET`

**Endpoint URL:** `/users/`

**Arguments:** Not required

**Full route path URL:** `http://127.0.0.1:5000/users/`

**Authentication:** No auth required.

**Expected request body (JSON):** Not required

**Expected response body:**

```json
[
	{
		"id": 1,
		"username": "user1",
		"join_date": "07-08-2023"
	},
	{
		"id": 2,
		"username": "user2",
		"join_date": "07-08-2023"
	}
]
```

### Fetch single user

**Purpose:** Fetches information of a single user in the Cinematica API.

**HTTP method:** `GET`

**Endpoint URL:** `/users/<int:user_id>`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1`

**Authentication:** No auth required.

**Expected request body (JSON):** Not required

**Expected response body:**

```json
{
	"id": 1,
	"username": "user1",
	"join_date": "06-08-2023"
}
```

**Expected error response:**

When a user cannot be found.

```json
{
	"error": "User with ID of 11 cannot be found, please try again"
}
```

### Create new user

**Purpose:** Allows new users to create and register a new account in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/users/`

**Arguments:** Not required.

**Full route path URL:** `http://127.0.0.1:5000/users`

**Authentication:** No auth required, but upon successful registration, a user is provided with an access token they can use straight away.

**Expected request body (JSON):**

Both email and username must be unique.
All fields required.

```json
{
	"email": "user3@mail.com",
	"username": "user3",
	"password": "user3pw"
}
```

**Expected response body:**

```json
{
	"message": "You have sucessfully registered!",
	"new_user": {
		"id": 3,
		"username": "user3",
		"join_date": "06-08-2023"
	},
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTI4NTQxNiwianRpIjoiMDk2MmJjYTgtNGRkYy00NzQ2LWE3ODMtMmZiOWY1MjQ5YzhiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2OTEyODU0MTYsImV4cCI6MTY5MTM3MTgxNn0.QZVMtYuy8gwy3nSF9KMNtWHU6CTbfXchAx8AI794Vsc",
	"expiry": "24 hrs"
}
```

**Expected error responses:**

When an email is already taken.

```json
{
	"error": "Email already registered, please try again"
}
```

When a username is already taken

```json
{
	"error": "user3 is already registered, please try again"
}
```

### Update user information

**Purpose:** Allows users to update and make changes to their account information.

**HTTP method:** `PUT`, `PATCH`

**Endpoint URL:** `/users/<int:user_id>`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user to perform updating and making changes to their own account.

**Expected request body (JSON):**

Both email and username must be unique.
Not all fields are required, can do one of three.

```json
{
	"email": "user3new@mail.com",
	"username": "user3new",
	"password": "user3new"
}
```

**Expected response body:**

Password included to update

```json
{
	"message": "Account update successful!",
	"user": {
		"user_id": 3,
		"email": "user3new@mail.com",
		"username": "user3new",
		"password": "Password updated"
	}
}
```

Password excluded when updating user info

```json
{
	"message": "Account update successful!",
	"user": {
		"user_id": 3,
		"email": "user3new@mail.com",
		"username": "user3new",
		"password": "Password not updated"
	}
}
```

**Expected error responses:**

When updating the email with the registered email of another user.

```json
{
	"error": "Email is already registered, please try again"
}
```

When updating the email with the current exisiting email.

```json
{
	"error": "Cannot update, new email matches with current email, please try another email"
}
```

When updating a username with current existing username.

```json
{
	"error": "Update failed, new username matches with current username, please try another username"
}
```

When updating an username with the registered username of another user.

```json
{
	"error": "user1 is already registered, please try again"
}
```

When updating a password with current existing password.

```json
{
	"error": "Password can't be the same as current password, please try again"
}
```

### Delete user

**Purpose:** Allows a user to delete/remove their own account from Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/users/user_id`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user to perform deleting their own account.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "You have sucessfully registered!",
	"new_user": {
		"id": 3,
		"username": "user3",
		"join_date": "06-08-2023"
	},
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTI4NTQxNiwianRpIjoiMDk2MmJjYTgtNGRkYy00NzQ2LWE3ODMtMmZiOWY1MjQ5YzhiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2OTEyODU0MTYsImV4cCI6MTY5MTM3MTgxNn0.QZVMtYuy8gwy3nSF9KMNtWHU6CTbfXchAx8AI794Vsc",
	"expiry": "24 hrs"
}
```

**Expected error response:**

When an email is already taken.

```json
{
	"error": "Email already registered, please try again"
}
```

When a username is already taken

```json
{
	"error": "user3 is already registered, please try again"
}
```

---

## Movie

The movie component of the Cinematica API contains several endpoints that involves fetching information of either all movies or a single movie available in the Cinematica API. Additionally, endpoints for the creation of a movie is available as well as updating a specific movie’s information and lastly deleting the movie from the API completely.

### Fetch all movies

**Purpose:** Allows for both users and general public using the API to fetch all available movies from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/movies/`

**Arguments:** Not required.

**Full route path URL:** `http://127.0.0.1:5000/movies`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"total_movies": 7,
	"movies": [
		{
			"movie_id": 1,
			"title": "Inception",
			"director": "Christopher Nolan",
			"genre": "Drama/Sci-Fi",
			"runtime": "148 min",
			"release_year": 2010
		},
		etc...
	]
}
```

**Expecetd error responses:** No error response.

### Fetch single movie

**Purpose:** Allows for both users and general public using the API to fetch a single movie from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/movies/movie_id`

**Arguments:** `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/movies/4`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"movie_id": 4,
	"title": "Jaws",
	"director": "Steven Spielberg",
	"genre": "Adventure/Thriller",
	"runtime": "124 min",
	"release_year": 1975
}
```

**Expected error responses:**

When movie cannot be found.

```json
{
	"error": "Movie with ID of 43 cannot be found, please try again"
}
```

### Create new movie

**Purpose:** Allows for a registered and authenticated user to create and add a new movie into the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/movies/`

**Arguments:** Not required

**Full route path URL:** `http://127.0.0.1:5000/movies/`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user to perform the action to create a new movie to add to the Cinematica API.

**Expected request body (JSON):**

All fields are required.
The same movie title can have different directors attached but a movie under one title cannot have the same directors.

```json
{
	"title": "New movie",
	"director": "New director",
	"genre": "Action",
	"runtime": "127 min",
	"release_year": "2037"
}
```

**Expected response body:**

```json
{
	"message": "Movie successfully added!",
	"new_movie": {
		"movie_id": 8,
		"title": "New movie",
		"director": "New director",
		"genre": "Action",
		"runtime": "127 min",
		"release_year": 2037
	}
}
```

**Expected error responses:**

When movie with the same director already exists.

```json
{
	"error": "Movie with the same director already exists, please try again"
}
```

### Update movie information

**Purpose:** Allows for a registered and authenticated user to update and make changes to a movie’s information in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/movies/movie_id`

**Arguments:** `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/movies/8`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user to perform the action to update a movie in the Cinematica API.

**Expected request body (JSON):**

Any one of the fields can be updated, not required to update all fields.

```json
{
	"title": "The Lord of The Rings: The Return of The King",
	"director": "Peter Jackson",
	"genre": "Fantasy/Adventure/Drama",
	"runtime": "210 min",
	"release_year": "2003"
}
```

**Expected response body:**

Before changes and updates are made

```json
{
	"title": "New movie",
	"director": "New director",
	"genre": "Action",
	"runtime": "127 min",
	"release_year": "2037"
}
```

After updated changes

```json
{
	"message": "Movie successfully updated!",
	"movie": {
		"movie_id": 8,
		"title": "The Lord of The Rings: The Return of The King",
		"director": "Peter Jackson",
		"genre": "Fantasy/Adventure/Drama",
		"runtime": "210 min",
		"release_year": 2003
	}
}
```

**Expected error responses:**

When movie cannot be found.

```json
{
	"error": "Movie with ID of 9 cannot be found, please try again"
}
```

When a movie with the same title and director already exists.

```json
{
	"error": "Movie with the same director and title already exists, please try again."
}
```

### Delete movie

**Purpose:** Allows for a registered and authenticated user to delete/remove a movie in the Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/movies/<movie_id>/`

**Arguments:** `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/movies/8`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user to perform the action to delete a movie in the Cinematica API.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "The Lord of The Rings: The Return of The King successfully deleted!"
}
```

**Expected error responses:**

When movie cannot be found.

```json
{
	"error": "Movie with ID of 8 cannot be found, please try again"
}
```

---

## Watchlist

The watchlist component of the Cinematica API contains several endpoints that involves fetching a specified users watchlist available in the Cinematica API. Additionally, endpoints for the adding a movie is available as well as updating the watchlist by bulk adding a collection of movies and lastly deleting the movie from the watchlist.

### Fetch user watchlist

**Purpose:** Allows for both users and the general public using the API to fetch a specific users watchlist of movies from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/users/<user_id>/watchlist/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/watchlist`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"total_movies": "2 movies in user1's watchlist",
	"watchlist": {
		"movies": [
			{
				"movie_id": 5,
				"title": "Oppenheimer",
				"added_to_watchlist": "07-08-2023"
			},
			{
				"movie_id": 6,
				"title": "Barbie",
				"added_to_watchlist": "07-08-2023"
			}
		]
	}
}
```

**Expected error responses:**

When no movies are found in the watchlist.

```json
{
	"error": "No movies found in user1's watchlist, please try again"
}
```

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

### Add movie to watchlist

**Purpose:** Allows for a registered and authenticated user to add a movie to their watchlist in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/users/<user_id>/watchlist/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/watchlist/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the watchlist in order to perform the action of adding a movie to their own watchlist in the Cinematica API.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "Barbie successfully added to watchlist",
	"movie": {
		"movie_id": 6,
		"title": "Barbie",
		"director": "Greta Gerwig",
		"genre": "Comedy/Drama",
		"runtime": "114 min",
		"release_year": 2023
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s watchlist.

```json
{
	"error": "You are not authorised to add or make changes to this watchlist"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to add a movie that already exists in the watchlist.

```json
{
	"error": "Barbie is already in this watchlist"
}
```

### Bulk add movies to watchlist

**Purpose:** Allows for a registered and authenticated user to add more than one movie to their watchlist in the Cinematica API.

**HTTP method:** `PUT, PATCH`

**Endpoint URL:** `/users/<user_id>/watchlist/movies/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/watchlist/movies/`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the watchlist in order to perform the action of bulk adding a movie to their own watchlist in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"list_of_movie_ids": [1, 3]
}
```

**Expected response body:**

```json
	"message": "2 movies added to watchlist",
	"movies": [
		{
			"movie_id": 1,
			"title": "Inception"
		},
		{
			"movie_id": 3,
			"title": "Psycho"
		}
	]
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add movies to another user’s watchlist.

```json
{
	"error": "You are not authorised to update or make changes to this watchlist"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When field data is left empty.

```json
{
	"list_of_movie_ids": ["List of movie ID's must not be empty, please try again"]
}
```

**Other responses:**

When adding movies that already exists in the watchlist.

```json
{
	"message": "These movies are already in the watchlist",
	"already_in_watchlist": [
		{
			"movie_id": 1,
			"title": "Inception"
		},
		{
			"movie_id": 3,
			"title": "Psycho"
		}
	]
}
```

When trying to bulk add multiple movies, and some already exists but some are yet to be added.

**Expected request:**

```json
{
	"list_of_movie_ids": [1, 3, 5, 6, 2]
}
```

**Expected response:**

```json
{
	"message": "2 movies added to watchlist but some are already exists in the watchlist",
	"movies": [
		{
			"movie_id": 5,
			"title": "Oppenheimer"
		},
		{
			"movie_id": 2,
			"title": "Spiderman"
		}
	],
	"already_in_watchlist": [
		{
			"movie_id": 1,
			"title": "Inception"
		},
		{
			"movie_id": 3,
			"title": "Psycho"
		},
		{
			"movie_id": 6,
			"title": "Barbie"
		}
	]
}
```

### Delete movie from watchlist

**Purpose:** Allows for a registered and authenticated user to delete/remove a movie to their watchlist in the Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/users/<user_id>/watchlist/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/watchlist/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the watchlist in order to perform the action of adding a movie to their own watchlist in the Cinematica API.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "Oppenheimer sucessfully removed from watchlist",
	"movie": {
		"movie_id": 5,
		"title": "Oppenheimer",
		"director": "Christopher Nolan",
		"genre": "Drama/Thriller",
		"runtime": "180 min",
		"release_year": 2023
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to delete/remove a movie to a another user’s watchlist.

```json
{
	"error": "You are not authorised to remove or make changes to this watchlist"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to remove a movie that isn’t in the watchlist

```json
{
	"error": "Barbie not found in watchlist to remove"
}
```

---

## Movielog

The movielog component of the Cinematica API contains several endpoints that involves fetching a specified users movielog available in the Cinematica API. Additionally, endpoints for the adding a movie is available as well as updating the movielog by bulk adding a collection of movies and lastly deleting the movie from the watchlist.

### Fetch user movielog

**Purpose:** Allows for both users and the general public using the API to fetch a specific users movielog of movies from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/users/<user_id>/movielog/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/movielog`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"total_movies": "1 movie in user1's movielog",
	"movielog": {
		"movies": [
			{
				"movie_id": 3,
				"title": "Psycho",
				"director": "Alfred Hithcock",
				"genre": "Horror/Thriller",
				"runtime": "109 min",
				"release_year": 1960,
				"added_to_movielog": "07-08-2023"
			}
		]
	}
}
```

**Expected error responses:**

When no movies are found in the watchlist.

```json
{
	"error": "No movies found in user1's watchlist, please try again"
}
```

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

### Add movie to movielog

**Purpose:** Allows for a registered and authenticated user to add a movie to their watchlist in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/users/<user_id>/movielog/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/movielog/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movielog in order to perform the action of adding a movie to their own movielog in the Cinematica API.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "Psycho added to movielog",
	"movie": {
		"movie_id": 3,
		"title": "Psycho",
		"director": "Alfred Hithcock",
		"genre": "Horror/Thriller",
		"runtime": "109 min",
		"release_year": 1960
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s movielog.

```json
{
	"error": "You are not authorised to add or make changes to this movielog"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to add a movie that already exists in the movielog.

```json
{
	"error": "Psycho is already in this movielog"
}
```

### Bulk add movies to watchlist

**Purpose:** Allows for a registered and authenticated user to add more than one movie to their movielog in the Cinematica API.

**HTTP method:** `PUT, PATCH`

**Endpoint URL:** `/users/<user_id>/movielog/movies/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/movielog/movies/`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movielog in order to perform the action of bulk adding a movie to their own movielog in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"list_of_movie_ids": [2, 4]
}
```

**Expected response body:**

```json
	"message": "2 movies added to watchlist",
	"movies": [
		{
			"movie_id": 2,
			"title": "Spiderman"
		},
		{
			"movie_id": 4,
			"title": "Jaws"
		}
	]
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add movies to another user’s movielog.

```json
{
	"error": "You are not authorised to update or make changes to this movielog"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When field data is left empty.

```json
{
	"list_of_movie_ids": ["List of movie ID's must not be empty, please try again"]
}
```

**Other responses:**

When adding movies that already exists in the movielog.

```json
{
	"message": "These movies are already in the movielog",
	"already_in_movielog": [
		{
			"movie_id": 2,
			"title": "Spiderman"
		},
		{
			"movie_id": 4,
			"title": "Jaws"
		}
	]
}
```

When trying to bulk add multiple movies, and some already exists but some are yet to be added.

**Expected request:**

```json
{
	"list_of_movie_ids": [1, 3, 5, 6, 2]
}
```

**Expected response:**

```json
{
	"message": "3 movies added to watchlist but some are already exists in the watchlist",
	"movies": [
		{
			"movie_id": 5,
			"title": "Oppenheimer"
		},
		{
			"movie_id": 6,
			"title": "Barbie"
		},
		{
			"movie_id": 7,
			"title": "The Apartment"
		}
	],
	"already_in_watchlist": [
		{
			"movie_id": 2,
			"title": "Spiderman"
		},
		{
			"movie_id": 4,
			"title": "Jaws"
		}
	]
}
```

### Delete movie from movielog

**Purpose:** Allows for a registered and authenticated user to delete/remove a movie to their movielog in the Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/users/<user_id>/movielog/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/movielog/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movielog in order to perform the action of adding a movie to their own movielog in the Cinematica API.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"message": "Jaws successfully removed from movielog!",
	"movie": {
		"movie_id": 4,
		"title": "Jaws",
		"director": "Steven Spielberg",
		"genre": "Adventure/Thriller",
		"runtime": "124 min",
		"release_year": 1975
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to delete/remove a movie to a another user’s watchlist.

```json
{
	"error": "You are not authorised to remove or make changes to this watchlist"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to remove a movie that isn’t in the watchlist

```json
{
	"error": "Jaws not found in movielog to remove"
}
```

---

## Rating

The rating component of the Cinematica API contains several endpoints that involves fetching a specified users movie ratings available in the Cinematica API. Additionally, endpoints for the adding a new movie rating is available as well as updating the ratings and lastly deleting/removing the rating for a movie.

### Fetch user ratings

**Purpose:** Allows for both users and the general public using the API to fetch a specific users ratings of movies from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/users/<user_id>/ratings/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/ratings`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"total_movies": "1 movie in user1's movielog",
	"movielog": {
		"movies": [
			{
				"movie_id": 3,
				"title": "Psycho",
				"director": "Alfred Hithcock",
				"genre": "Horror/Thriller",
				"runtime": "109 min",
				"release_year": 1960,
				"added_to_movielog": "07-08-2023"
			}
		]
	}
}
```

**Expected error responses:**

When no movie ratings are found.

```json
{
	"error": "No ratings found for user1, please try again"
}
```

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

### Add rating

**Purpose:** Allows for a registered and authenticated user to add a movie rating in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/users/<user_id>/ratings/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/ratings/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie ratings in order to perform the action of adding a movie to their own ratings in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"rating_score": 3
}
```

**Expected response body:**

```json
{
	"message": "Inception added to ratings!",
	"rating": {
		"rating_score": "3/5",
		"rating_date": "08-08-2023",
		"movie": {
			"movie_id": 1,
			"title": "Inception"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s ratings.

```json
{
	"error": "You are not authorised to add or make changes to this users ratings"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to rate a movie that has already been rated by the user.

```json
{
	"error": "Inception has already been rated"
}
```

### Update rating

**Purpose:** Allows for a registered and authenticated user to update a movie’s rating in the Cinematica API.

**HTTP method:** `PUT`

**Endpoint URL:** `/users/<user_id>/ratings/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/ratings/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie ratings in order to perform the action of updating a movie to their own ratings in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"rating_score": 5
}
```

**Expected response body:**

```json
{
	"message": "Rating for Inception successfully updated!",
	"rating": {
		"rating_score": "5/5",
		"rating_date": "08-08-2023",
		"movie": {
			"movie_id": 1,
			"title": "Inception"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s ratings.

```json
{
	"error": "You are not authorised to update or make changes to this users ratings"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to update a movie’s rating that has not been rated by the user.

```json
{
	"error": "No existing rating found for Spiderman"
}
```

### Delete rating

**Purpose:** Allows for a registered and authenticated user to delete/remove a movie’s rating in the Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/users/<user_id>/ratings/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/ratings/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie ratings in order to perform the action of deleting/removing a movie to their own ratings in the Cinematica API.

**Expected request body (JSON):** Not required

**Expected response body:**

```json
{
	"message": "Rating for Inception successfully updated!",
	"rating": {
		"rating_score": "5/5",
		"rating_date": "08-08-2023",
		"movie": {
			"movie_id": 1,
			"title": "Inception"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to remove a movie of a another user’s movie ratings.

```json
{
	"error": "You are not authorised to remove or make changes to this users ratings"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to delete a movie’s rating that has not been rated by the user.

```json
{
	"error": "No existing rating found for Inception"
}
```

---

## Review

The reviews component of the Cinematica API contains several endpoints that involves fetching a specified users movie reviews available in the Cinematica API. Additionally, endpoints for the adding a new movie review is available as well as updating the reviews and lastly deleting/removing the review for a movie.

### Fetch user reviews

**Purpose:** Allows for both users and the general public using the API to fetch a specific users reviews of movies from Cinematica.

**HTTP method:** `GET`

**Endpoint URL:** `/users/<user_id>/reviews/`

**Arguments:** `user_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/reviews`

**Authentication:** Not required.

**Expected request body (JSON):** Not required.

**Expected response body:**

```json
{
	"total_movies": "1 movie in user1's movielog",
	"movielog": {
		"movies": [
			{
				"movie_id": 3,
				"title": "Psycho",
				"director": "Alfred Hithcock",
				"genre": "Horror/Thriller",
				"runtime": "109 min",
				"release_year": 1960,
				"added_to_movielog": "07-08-2023"
			}
		]
	}
}
```

**Expected error responses:**

When no movie reviews are found.

```json
{
	"error": "No reviews found for user1, please try again"
}
```

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

### Add review

**Purpose:** Allows for a registered and authenticated user to add a movie review in the Cinematica API.

**HTTP method:** `POST`

**Endpoint URL:** `/users/<user_id>/review/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/review/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie reviews in order to perform the action of adding a movie to their own reviews in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"review_text": "Meh, this movie was average.."
}
```

**Expected response body:**

```json
{
	"message": "Oppenheimer added to ratings!",
	"review": {
		"review_text": "Meh, this movie was average..",
		"review_date": "08-08-2023",
		"movie": {
			"movie_id": 5,
			"title": "Oppenheimer"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s reviews.

```json
{
	"error": "You are not authorised to add or make changes to this users reviews"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to rate a movie that has already been reviewed by the user.

```json
{
	"error": "Oppenheimer has already been reviewed"
}
```

### Update review

**Purpose:** Allows for a registered and authenticated user to update a movie’s review in the Cinematica API.

**HTTP method:** `PUT`

**Endpoint URL:** `/users/<user_id>/reviews/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/reviews/movies/<movie_id>`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie reviews in order to perform the action of updating a movie to their own reviews in the Cinematica API.

**Expected request body (JSON):**

```json
{
	"review_text": "Fantastic movie, cinematic masterpiece!"
}
```

**Expected response body:**

```json
{
	"message": "Review for Oppenheimer sucessfully updated!",
	"review": {
		"review_text": "Fantastic movie, cinematic masterpiece!",
		"review_date": "08-08-2023",
		"movie": {
			"movie_id": 5,
			"title": "Oppenheimer"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to add a movie to a another user’s ratings.

```json
{
	"error": "You are not authorised to update or make changes to this users ratings"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to update a movie’s rating that has not been reviewed by the user.

```json
{
	"error": "No existing review found for Barbie"
}
```

### Delete review

**Purpose:** Allows for a registered and authenticated user to delete/remove a movie’s review in the Cinematica API.

**HTTP method:** `DELETE`

**Endpoint URL:** `/users/<user_id>/reviews/movies/<movie_id>`

**Arguments:** `user_id` (integer), `movie_id` (integer)

**Full route path URL:** `http://127.0.0.1:5000/users/1/reviews/movies/5`

**Authentication:** Bearer access token is required in the authorisation header in order to authenticate if the user is registered and authorise the user if they are the owner of the movie reviews in order to perform the action of deleting/removing a movie to their own reviews in the Cinematica API.

**Expected request body (JSON):** Not required

**Expected response body:**

```json
{
	"message": "Review successfully removed!",
	"deleted_review": {
		"review_text": "Fantastic movie, cinematic masterpiece!",
		"review_date": "08-08-2023",
		"movie": {
			"movie_id": 5,
			"title": "Oppenheimer"
		}
	}
}
```

**Expected error responses:**

If user doesn’t exist.

```json
{
	"error": "User with ID of 44 cannot be found, please try again"
}
```

When trying to remove a movie of a another user’s movie reviews.

```json
{
	"error": "You are not authorised to remove or make changes to this users reviews"
}
```

If movie doesn’t exist.

```json
{
	"error": "Movie with ID 55 cannot be found, please try again"
}
```

When trying to delete a movie’s review that has not been rated by the user.

```json
{
	"error": "No existing review found for Oppenheimer"
}
```
