# Cinematica API

A RESTful API for movie enthusiasts to review, rate and keep track of movies throughout their cinematic journey.

This project is developed as an assignment for Coder Academy, it being an API webserver, there is no front-end implemented. To test the functionality of the API, you can use API client testing tools such as Postman or Insomnia to have a UI to test the API endpoints on.

---
## [GitHub repo](https://github.com/jordansbenjamin/Cinematica_API)

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

## R5: API Endpoints Documentation

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

---

## R1/R2: Identification of the _problem_ you are trying to solve by building this particular _app_ and why is it a *problem* that needs solving?

Cinematica is a web app and social platform directed towards movie buffs and enthusiasts where they’re able to come together and share their own watchlist of movies, reviews they’ve written and movie ratings to other users of the platform.

While there is a social connection aspect to the app, the ability for users to store movies they’ve watched and keep a watchlist of movies, and even a platform where they’re able to store reviews of movies and ratings as a form of journal in their cinematic journey works really well for those in need of a all-in-one tracking platform. And if they wish to use the social aspect of the app, then its only a click away from interacting with like-minded movie enthusiasts.

### A problem already solved

This solves the problem of bringing together the various cinematic communities, from those who loves horror films, comedies, rom-coms, and even indie films to come together to share their thoughts on the movies they love and also have differences in. But it also caters towards the individual who seeks for a platform to store their own thoughts as a form of journal or tracker that they can easily come back to, or for other users to explore.

This concept has of course been attempted to great success each with their own unique features, with platforms such as IMDB, Rottentomatoes and the newly popular Letterboxd. Which at the core allows users to rate and review movies, and for other users to view them and interact with as well.

While IMDB and Rottentomatoes are more geared towards industry reach, with the support of movie critics and industry professionals to be credited in the films they worked in, its most favoured features lies in the ability for the general moviegoers to rate and give reviews to movies as well. Which has become a popular source for moviegoers to determine whether or not a film is worth watching.

Letterboxd in fact, excels in this aspect where it provides a much more personalised experience, its focus lies in the social network of the application where users are able to follow other users, a rating system not just for the movies but the users reviews as well which motivates users to write great (or hilarious) reviews.

There are in fact many more features that Letterboxd has to offer, but I wanted to point out that the social network aspect that Letterboxd provides to its users is exactly what the Cinematica app hopes to not only achieve but extends its features even further.

### New problems to solve

So, while platforms like IMDb, Rotten Tomatoes, and Letterboxd provide some of the features which allows users to track their cinematic journey, journal their thoughts, and connect with like-minded individuals. They fall short in delivering an all-inclusive experience that caters to both personal and social aspects of a movie enthusiast's journey.

These existing platforms have limitations such as lack of personalised user experience, absence of community-building features like in-app messaging and forums, and inadequate tools for nuanced film analysis. In addition, users have expressed a desire for direct integration with streaming platforms and gamification elements which are lacking in current solutions.

The Letterboxd community itself has grown quite large and a portion of the community have spoken on improvements the platform should make to provide a better user experience and any recommendations to the functionalities and performance of the platform itself.

### Achieving the MVP

As a web app, Cinematica will achieve the minimum viable product of being able to provide its users to:

- Add movies to their watchlist
- Add and log movies they’ve watched to their MovieLog
- Write movie reviews
- Give ratings to movies

On top of that, if a user knows other users, they are able to search that user and see their reviews, ratings, and watchlists as well.

However, while planning the application and the API originally, instead of saving the movies entire information such as the cinematic properties like the title, director, genre, release year, etc. the only information that will be stored within that entity is the unique Movie_ID.

This ID matches the movies ID in the external API from which the movie data was to be outsourced from. By only storing the movie ID, this helps with avoiding redundancy and potentially having outdated data in the apps database.

However, after some careful consideration and feedback, Cinematica will not include the call of an external API but rather include the feature of having manual and user inputted movie data with the Cinematica API. This way, Cinematica will be able to establish and meet the requirement of the MVP and will consider the use of fetching movie data from an external API in future implementations.

With this, Cinematica will focus on the establishing a much more personalised experience for users of the app, allowing the user the freedom to input data of movies they wish to add. This can be a movie that exists in most databases, to niches independent films that doesn’t exist or as well known, to even the users own movies.

### Features of the future

Cinematica plans to develop overtime to include many more features that will meet the same functionalities to that of our potential competitor, Letterboxd, currently provides (to name a few):

- The ability for users to follow other users
- Users are able to comment on other users reviews
- Like/rate other users watchlists
- Personalised statistics for users
- Recommendation system
- External API movie database implementation

More importantly, in the future, Cinematica will provide the experience users are lacking at existing platforms. Cinematica will address these features in the future:

- Users are able to send messages to each other
- An inbuilt forum that extends beyond just reviewing movies where users are able to extend their conversations within the community
- Custom rating system (Users are able to not only rate the movie overall, but rate on specific aspects of the movie, such as performance, cinematography, costume design, etc. This allows for a more nuanced and accurate review, which helps with data collection for the recommendation system)
- Badges and achievements, a gamification for users to receive rewards for the amount of movies they have watched, writing a certain number of reviews, etc.
- Integration with streaming platform, this is the feature that is requested highly by Letterboxd users, and something we hope to achieve before they do as it will provide a much more seamless experience for users, where movies are automatically added to their watched movies list when using supported streaming platforms.

### The solution

The focus of course comes back down to providing a minimum viable product in providing a platform for users to track and manage movies they’ve watched, a watchlist of movies and giving reviews and ratings. This will be at the core of the Cinematica web app.

Cinematica aims to fill the gaps by providing a robust platform that caters to all aspects of a movie enthusiast's needs. Our platform will not only allow users to manage their watchlist and track movies they've watched, but also provide them with a space to write detailed reviews and ratings.

Furthermore, Cinematica will foster a community of movie lovers by facilitating connections between users through features like user search, followers, comments, and future in-app messaging and forum functionalities.

Cinematica, at its core, will provide a personalized experience for each user. As we evolve, we'll incorporate more advanced features like custom rating systems for nuanced reviews, badges and achievements for user engagement, and direct integration with streaming platforms for seamless tracking of watched content.

---

## R3: Why have you chosen this database system. What are the drawbacks compared to others?

For the Cinematica app, the first database management system that comes to mind to utilise is PostgreSQL.

### Choosing PostgreSQL

The choice of using PostgreSQL as the database system is its compatibility with Flask, the framework that will be used and written in conjunction with Python to develop the application. PostgreSQL’s compatibility with Flask is the result of the third party services available to use with Flask such as SQLAlchemy (which will be explored more in dept shortly) and marshmallow as well, all to support and extend the functionalities and interactions with PostgreSQL.

PostgreSQL is a Relational Database Management System, which is a DBMS that adopts the relational database model which allows for the creation of storing data in relations. Relations are an incredibly important aspect of a RDBMS as it helps manages and structure data into tables (relations). Tables which are quite familiar, tables with columns and rows, with each table representing an entity. The columns represent the attributes of the table, and the row represents the records of data.

### Normalisation

Storing and organising data into relations allows for consistency and keeps their value and integrity. This is first done with a process called normalisation, which reduces data redundancy and improves data integrity. Not only data will be more consistent and stable, normalising data in the relational database model allows the ability to perform complex queries.

### Entities & ERD

This is due to the important aspect of relationships between entities (tables/relations) which is established when designing the database schema, this relationship is represented by what is known as an Entity Relationship Diagram. Where each entity is visually represented in tables and connections of the different relationships and interactions of each entity is made.

### Relationships

Relationships are established through unique identifiers such as the primary and foreign keys, which represents the connection between entities. And it is through the keys, that a database such as PostgreSQL is able to make rather complex and powerful queries.

### SQL / manipulating data

Speaking of queries, PostgreSQL uses the Structured Query Language to perform database operations and manipulating data, these operations are commonly referred to as CRUD operations which involves reading, creating, updating and deleting data. SQL allows you to do just that with its own rather simple english like syntax, but its ability to perform complex and powerful queries and the fact that SQL is standardised makes it much easier to move from one RDBMS to another.

### Open source

PostgreSQL is open source, free and readily available to use. With that in mind, PSQL is not owned by an organisation with a lot of its support coming from the community themselves with over thirty years growing this community, there is an incredible amount of support tools, resources and documentation readily available.

### ACID compliant

There are of course many more benefits of using PSQL but I want to end with mentioning PostgreSQL being a relational database management system comes with the great benefit of being ACID compliant. ACID stands for atomicity, consistency, isolation and durability.

PostgreSQL being ACID compliant allows for reinforcing its data integrity as a database which more than usually manages sensitive user information. ACID properties themselves ensures that any transactions and processes occurring in the database for it to be completed entirely or none at all. It’s an all or nothing system to ensure that data doesn’t get lost during transaction which prevents from any inconsistencies.

When something does occur and the integrity of the data is in danger, ACID ensures to handle this accordingly, even at the event of a system failure.

### Drawbacks

Of course, PostgreSQL doesn’t come without its drawbacks. One notable drawback of using PostgreSQL funnily enough comes from its very own wide range of features, which, for new developers can be complex to understand and navigate at first which in turn results in using PostgreSQL quite overwhelming. Setting up PostgreSQL at the start does quite a bit more time and configuration for setting up the database for use.

Another notable drawback, is the slow performance which is known for SQL databases. Despite it performing extremely well for complex queries and management and organisation of large datasets and databases, it suffers in performance even when performing simple read and write operations. But the consideration of performance comes from the specific use cases of the database (PSQL) itself and that will determine and impact its performance.

This is comparing PostgreSQL’s slow speed with NoSQL (non-relational) databases such as MongoDB but also with SQL databases such as MySQL itself. So it really does depend on the DBMS itself but more importantly the amount of data and the types of operations being performed in the database impacts the speed as well.

On that note, a DBMS like MongoDB doesn’t require for setting up the overall structure of the database as in dept as you would with PSQL, this is due to the flexibility of the schema structure of NoSQL databases. It is much faster to get a NoSQL database such as MongoDB up and running.

Some more known drawbacks of PSQL:

- Known to be more memory intensive than some lighter-weight relational databases.

- While PostgreSQL has a rich set of extensions and integrations, it might not be as vast as some other more popular databases.

- Depending on the dataset size, backup and restore operations might take longer compared to some other databases.

- Some software systems, especially legacy ones, might not have out-of-the-box support for PostgreSQL.

- While there are some, the quality and features of GUI-based management tools might not be as extensive or intuitive as those available for other databases, mySQL is one example.

### Concluding

For the Cinematica app, PostgreSQL is a fitting choice. It's robust, free, comes with many features and is scalable which is crucial for smaller to larger scale web applications. Its scalability can be more complex compared to NoSQL databases, but it's possible and very efficient once properly set up. PostgreSQL's open-source nature allows for great flexibility and customisation, which is valuable. And its definitely safe to say that good outweighs the bad in choosing PostgreSQL as a RDBMS.

---

## R4: Identify and discuss the key functionalities and benefits of an ORM

### An overview

With Flask as the web framework and PostgreSQL as the database in mind, the Cinematica API will be using a programming technique called Object Relational Mapping or ORM for short which is mentioned very briefly before. An ORM essentially helps establishes the connection required between the database and the language (in this case Python) the application is developed in.

Specifically, it taps into the object orienting programming aspect of the language as a way to communicate with the database, bridging the gap between the program and the database through OOP principles of the language in use.

Operations performed on relational databases are of course done through SQL, allowing for CRUD operations to be performed to query data from the database. While this is perfectly adequate, a tool such an ORM provides an alternate method of interaction with the database with the familiarity of the programs OOP language.

This allows for a much more efficient (because of the familiarity of the language) and also flexible approach in working with data along with the interactions with the database as ORM’s allow for different approaches to performing queries. All to provide a much more streamlined implementation for the developer during the development process.

To put it simply, an ORM acts as bridge or intermediary between the program along with the code/logic written and the SQL database itself. In the case of the project, it helps connect Flask with PostgreSQL through the ORM.

One such ORM that is available for Flask is SQLAlchemy, this is the perfect pair when developing the Cinematica app because SQLAlchemy offers a high-level and Pythonic API that seamlessly integrates with Flask's structure. Furthermore, it supports PostgreSQL out of the box, making it incredibly straightforward to set up and maintain a robust connection between the app and the database.

This is a great benefit of using an ORM, it helps handle all the logic otherwise required to be written behind the scenes which supports in minimising the extra requirement to write logic for interacting with the database. All done without writing a single SQL statement. Instead it use the OOP principles provided by the ORM which is translated behind the scenes as SQL statements.

The benefit is not from completely avoiding from having to query data using SQL, but the organisation and OOP structure provided by an ORM helps in navigating, updating and maintaining the logic of programs interaction with the database. Essentially reducing boilerplate code which in turn leads to transferring all the focus on writing the program itself, and of course this efficiency leads to faster development cycles and overall productivity.

### Database models as classes

An ORM’s OOP principle also defines and maps relations as classes and objects, and because of this it allows for modelling the relationships in a way that reflects real-world scenarios. This ensures that data is consistent, relations are intact, and any change in one part of the data structure gets appropriately reflected in related areas, minimising inconsistencies and errors.

Here is an example of a model class defined in SQLAlchemy:

```python
class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(128), nullable=False)
	director = db.Column(db.String(64), nullable=False)
	genre = db.Column(db.String(32), nullable=False)
	runtime = db.Column(db.String(16), nullable=False)
	release_year = db.Column(db.Integer(), nullable=False)

	watchlists = db.relationship(
	'Watchlist', secondary=watchlist_movie_association, back_populates='movies')
	movielogs = db.relationship(
	'MovieLog', secondary=movielog_movie_association, back_populates='movies')

	reviews = db.relationship('Review', back_populates='movie')
	ratings = db.relationship('Rating', back_populates='movie')
```

Each attribute in the `Movie` class represents a column in the corresponding table in the database. `id`, `title`, `director`, `genre`, `runtime`, and `release_year` are straightforward fields with respective data types. Relationships such as `watchlists`, `movielogs`, `reviews`, and `ratings` represent the associations between the `Movie` class and other classes (`Watchlist`, `MovieLog`, `Review`, and `Rating`).

Creating models as classes in ORM has several advantages:

- It abstracts the underlying database structure and offers a Pythonic way to handle database operations.
- By defining relationships in a class, it's easier to visualise and understand how various tables (or models) relate with one another.
- These classes can be reused across different parts of the application, ensuring DRY (Don't Repeat Yourself) principles are maintained.
- Changes in a class structure or relationships can be seamlessly transferred to the database schema with migrations.

And here is the SQL equivalent of the model class above:

```sql
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    director VARCHAR(64) NOT NULL,
    genre VARCHAR(32) NOT NULL,
    runtime VARCHAR(16) NOT NULL,
    release_year INTEGER NOT NULL
);
-- Note: Relationships are not covered in this SQL example since they involve additional tables and foreign key constraints.
```

Some key differences between SQlAlchemy and raw SQL:

- The ORM version abstracts away many database specifics, while SQL is direct about the commands.
- SQL gives direct control over database operations while ORM offers a more generalised way to interact with the database.
- The ORM code showcases relationships seamlessly as part of the model, while in SQL, relationships often require additional commands and tables.
- For developers familiar with Python, the ORM version can be more intuitive. In contrast, those well-versed in SQL may find direct SQL commands clearer.

### Manipulating data with SQLAlchemy

Here are some examples of performing CRUD operations with comparisons with both SQL and SQLAlchemy, you can see that SQL statements are abstracted into the Python language and OOP concepts where SQLAlchemy transforms into SQL statements behind the scenes to perform queries with PostgreSQL.

#### Create

Here is an example for inserting a movie using SQL:

```sql
INSERT INTO movies (title, director, genre, runtime, release_year) VALUES ('Inception', 'Christopher Nolan', 'Sci-Fi', '148 min', 2010);
```

And here is the SQLAlchemy ORM equivalent:

```python
new_movie = Movie(
				  title='Inception',
				  director='Christopher Nolan',
				  genre='Sci-Fi',
				  runtime='148 min',
				  release_year=2010)
db.session.add(new_movie)
db.session.commit()
```

#### Read

Here is an example of SQL code for querying title of movies based on the director:

```sql
SELECT title FROM movies WHERE director = 'Christopher Nolan';
```

And here is the SQLAlchemy ORM equivalent:

```python
movies = Movie.query.filter_by(director='Christopher Nolan').all()
```

#### Update

Here is an example of updating a movie’s info using SQL:

```sql
UPDATE movies SET genre='Action' WHERE title = 'Inception';
```

And here is the SQLAlchemy ORM equivalent:

```sql
movie_to_update = Movie.query.filter_by(title='Inception').first()
movie_to_update.genre = 'Action'
db.session.commit()
```

#### Delete

Lastly, this is an example of deleting a movie based on its title using SQL:

```sql
DELETE FROM movies WHERE title = 'Inception';
```

And here is the SQLAlchemy ORM equivalent:

```python
movie_to_delete = Movie.query.filter_by(title='Inception').first()
db.session.delete(movie_to_delete)
db.session.commit()
```

#### Security

One common for security concern when it comes to validation of incoming data is the potential attack of what is known as a “SQL Injection”, which is where a bad actor is able to penetrate and insert their own SQL code to gain access to a database. When they access and they are able to view the sensitive information the database stores.

Depending on the sophistication of the SQL injections, they are able to go even further, manipulating the data and even worse, deleting it.

When it comes to SQL injections, an ORM such as SQLAlchemy allows us to use parameterised queries by default which means that the commands will always follow a specific pattern. This greatly reduces the risk of receiving information that either does not belong or information that wont be accepted based on the parameters set by an ORM such as SQLAlchemy.

#### Concluding

Its rather clear than an ORM provides great benefit to both the developer and the program itself, a great tool that helps with interacting with databases through OOP concepts and principles which provides in much more efficient processes and workflow (making it much easier to refactor or modify the overall schema if required) and overall code maintainability along with consideration to security as well.

An ORM such as SQLAlchemy is the perfect pair in developing the Cinematica app with Flask as the web framework and PostgreSQL as the relational database of choice.

### Summarising SQLAlchemy’s functionality & benefits

**Functionalities**:

- Define database models as Python classes, abstracting the underlying database schema.
- Supports powerful and flexible querying with a Pythonic syntax.
- Easily Create, Read, Update, and Delete records using object-oriented principles.
- Facilitates defining relationships between tables (e.g., one-to-one, one-to-many, many-to-many).
- Define columns with Python types, and SQLAlchemy manages the translation to database-specific types.
- Modify the database schema over time without losing data using Alembic, a database migration tool.
- Handle database transactions, allowing for grouped operations and safer commits or rollbacks.
- Offers aggregate functions and grouping capabilities.
- Provides a session for bundling a series of operations into a transaction.
- Handles efficient database connections, reusing connections when needed.

**Benefits**:

- Hides the complexity of direct SQL commands, allowing developers to think in object-oriented terms.
- Works with multiple database backends, making the application more database agnostic.
- ORM provides a consistent API to interact with varying databases, reducing errors.
- Reduces the amount of boilerplate code required, making development faster.
- Helps prevent SQL injection attacks by using bind parameters.
- Makes code more readable and maintainable by using Pythonic syntax for database operations.
- Models and operations can be easily reused across different parts of the application.
- Integrates smoothly with popular web frameworks like Flask and Django.
- Strong community support and extensive documentation available.
- Provides a plugin system that allows the addition of custom types and operations.

To summarise, an ORM such as SQLAlchemy bridges the gap between object-oriented programming and relational databases, ensuring efficient, organised, and secure interactions with the data. Whether it's translating high-level Pythonic queries into SQL, preventing SQL injections, or modeling complex relationships, an ORM, especially one as powerful as SQLAlchemy, provides a streamlined, robust, and secure foundation for building applications like Cinematica.

---

## R6: An ERD for your *app* & R9: Discuss the database relations to be implemented in your application

I have combined these two discussions as they represent the best of both worlds when discussing relations that will be implemented in Cinematica’s database schema whilst also referring to the ERD which visually represents these relations.

You will find below the final iteration for the Entity Relationship Diagram (ERD) that helped design the structure and schema of Cinematica’s database, the ERD represents a normalised database following normal forms of the normalisation process to avoid data redundancy and strengthen data integrity.

<img src="./docs/Cinematica-ERD_Final.jpg"></img>

Of course this being a relational database, each entity in the ERD represents all the different tables and its respective attributes along with their constraints as well. More importantly, this ERD adopts the crows foot notation as a database and ERD design process. Crows foot notation provides symbols that represents the four types of cardinality that an entity might have in a relationship.

If you wish to go through other iterations of the ERD, you can view them [*here*](https://github.com/jordansbenjamin/Cinematica_API/blob/main/docs/ERD-iterations.md).

### Discusing database relations

#### User

The User entity represents the user of the Cinematica API app, and the attributes of the entity itself represents personal information such as their username which they are able to choose and will be used as their main identity within the application, a password is also required as it will be used to authorise the user to access the main features of the application itself.

The user is required to sign up to be able to add movies to a watchlist or movielog, and for them to give review and ratings of movies. Without having an account with the Cinematica app, users are only able to view other users (if they know their ID) watchlist, reviews and ratings but not create their own.

Additionally, a Join_Date attribute helps establish the date the user first joined the application which in the future this data could be used for a rewards or loyalty system and in general a merit type reminder for either the user themselves or for other users to see how long they have used the app.

The user entity interacts with other entities of the application, starting with the rating entities, the relationship established allows users to give ratings to multiples movies of their choice. This relationship is defined as a one-mandatory to optional-many relationship starting from the user entity to the rating entity. Where for a movie to be rated, it must be rated by a user which is what the relationship describes.

The same relationship is established between the user entity and the review entity, where a user has the option to give multiple reviews to different movies but for a movie to be reviewed it must come from a user.

The relationship between the user and the watchlist entity is a one-mandatory to one-mandatory relationship. Only because in this MVP version of the app, the user is only able to have one main watchlist, of course in the future, customisation and the creation of multiple watchlists will be catered towards. So, for now, a user has the option to add movies to a single watchlist if they wish.

This one-mandatory to one-mandatory relationship is also established between the user and the movielog entity, where a user only has one movielog in this current MVP version of the app and the movielog only belongs to a single user.

There is an implicit relationship between the user and movie entities through the watchlist and movielog entities along with its respective association tables connecting them altogether. And additionally, the same could be said with connecting the user and movie entities through the rating and review entities. I just want to mention this now, but it will get more clear when explaining those other entities with how and why those relationships matter.

Attributes represented in the ERD:

- User_ID (Primary Key, Integer, Not Null)
- Email (String(128), Not Null, Unique)
- Username (String(128), Not Null, Unique)
- Password (String(64), Not Null)
- Join_Date (Date, Not Null, Default: Current Date)

The User_ID attribute represents the primary unique identifier (the primary key) that will be used throughout the database that connects the user entity and its relationship with other entities. Its data type is integer and its constraint is not null as the chosen database management system and ORM will handle both automatic incrementation of the ID value and also primary keys automatically have a not null constraint without having to explicitly set it.

The Email attribute represents the users email, and in this current MVP version, the email is used to simply store the users information from the get go, as in future updates, emails will be required for further authentication, password recovery, and email listings. It has a string data type with 128 characters constraint, along with not null and unique as well.

The Username attribute represents as the main unique text identifier for the users in Cinematica, this is where other users are able to easily identify a user based on a text username rather than ID number. Which both information will be provided for other users to view. It has a string data type with 128 characters constraint, along with not null and unique as well.

The password attribute will be used for authenticating and authorising the user, since certain components of the app requires a user to be registered, authenticated and authorised. It has a string data type with 64 characters constraint, along with not null.

Lastly the Join_Date attribute represents the exact date the user registered and joined the application, this information will be helpful to themselves but also Cinematica for use in future updates (rewards/loyalty system). It is of Date type, not null and with a default current date constraint.

#### Movie

The movie entity itself represents the information of the individual movies within the Cinematica API app. Users will be able to enter a movies information from a movies title, genre, director, runtime and the year its released.

While achieving the MVP of the Cinematica app, the attributes available to showcase the movies information would suffice in identifying the movie with improvements in future implementation could include but not limited to:

- A plot summary
- Cast
- Awards
- Age rating

Earlier, its established that the movie entity has a connection and relationship with the user entity through other entities. Those connections are made through the rating, review, watchlist and movielog entities.

This is the case because both the user and movie entities makes up the core of the Cinematica app, it being a movie watchlist/tracker and review/journal social network app.

The relationships established between the entities all combined makes up the entire functionality of the Cinematica app serving its purpose, the relationship starts of course with the user and it ends with the movies (the core of the app).

The movie entity will serve as an interface for users to add movies into the Cinematica apps database, and other users are able to contribute as well (of course validation will be enforced).

The relationship of the movie entity with other entities differ, for example, starting with the relationship established between the movie, watchlist and user entities. Starting with the user, who has exactly one watchlist, and that watchlist belongs to exactly that user, this we saw earlier is what established the mandatory-one to mandatory-one relationship.

Now a watchlist can have zero or more movies, the relationship established between the users watchlist and movie entity is done through an association table. Starting from the watchlist, its an optional-one (watchlist side) to optional-many (watchlist movie association table side). A watchlist can have zero or many movie associations. Every watchlist exists independently and can potentially have no movies, but if it does, it can have many.

This is exactly similar with the movie entity and its relationship with the watchlist entity connected via the association table, where it starts off with optional-one (movie side) to optional-many (watchlist movie association table side). Every movie can either not be in any watchlist or be in many. This signifies that while a movie exists, it doesn't necessarily need to be a part of a watchlist, but if it is, it can be in multiple watchlists.

The "optional" part here helps explain that while entities (either movies or watchlists) exist, they are not mandatorily associated with each other. A movie can exist without being in a watchlist and a watchlist can exist without having any movies.

What the association table ultimately achieves is the many-to-many relationship the watchlist and movie entity have with each other, since a watchlist can contain many movies, and many movies can be in multiple watchlists.

This relationship between the watchlist and movie entity is identical to the relationship the movie entity has with the movielog entity, it also has a movielog association table connecting the many-to-many relationship the two entities have.

This relationship is somewhat similar with the rating and review entities, where the movie entity side of the relationship begins with an optional-one, and the rating and review entities presents an optional-many. This ultimately creates an optional-one to optional-many relationship between the movie entity with the rating and review entities.

The relationship is established this way as for a rating or review for a movie to exist, it must have a movie attached to it, but a movie doesn’t need to have a rating or review hence it being optional-one, and it of course can be in multiple rating and reviews hence the optional-many. However, the only difference being that an association table is not required connecting the relationship of the movie entity with the rating and review entities.

Of course, the Movie_ID is required as this is the primary source of connecting those relationships and it serve as unique identifier (primary key) for the movie entity. This is where the optional-one from the movie entity starts, the Movie_ID being the primary key and it becomes a foreign key in both the rating and review entity but also the watchlist and movielog association tables.

Attributes represented in the ERD:

- Movie_ID (Primary Key, Integer, Not Null, Unique)
- Title (String(128), Not Null)
- Director (String(64), Not Null)
- Genre (String(32), Not Null)
- Runtime (String(16), Not Null)
- Release_year (Integer, Not Null)

#### Watchlist

The Watchlist entity represents a collection of movies that a user wishes to watch in the future. Each watchlist is tied to a unique User_ID, signifying the user who created the watchlist. This is the mandatory-one-to-mandatory-one relationship established between the user and watchlist entity where a user has the option to add movies to at least one watchlist and a watchlist must correspond to that user.

Additionally, each watchlist can contain zero, one or multiple Movie_IDs, each corresponding to a movie that the user has added to their watchlist. The connection between the movie and watchlist entity is an optional-many-to-optional-many relationship. As we saw earlier, this is done through the watchlist movie association table.

This essentially establishes a many to many relationship where in other words, a watchlist can exist with zero movies, and a movie doesn't have to be in any watchlist.

Its important to note that these relationships are possible because the User_ID and the Movie_ID exists as fields in the watchlist movie association entity serving as foreign keys, connecting and establishing the watchlist relationship between the movie and user entities.

From a technical implementation standpoint, when a user creates an account or logs in for the first time, automatically an empty watchlist is created for them. All its required for users to do is simply add and remove a movie of their choice. The attribute of Date_Added will show information of the date that the movie is added to the watchlist for their reference.

In future implementation of course its planned for users to be able to create and customise their own watchlist, but at the current MVP version, this is what the watchlist entity represents.

Attributes represented in the ERD:

- Watchlist_ID (Primary Key, Integer, Not Null)
- User_ID (Foreign Key, Integer, Not Null, References User(User_ID), unique)

##### Watchlist movie association (join table)

As discussed earlier in the movie and watchlist sections, a watchlist movie association is required to help bridge the many-to-many relationship the two entities have with each other.

Additionally, a Date_Added field is added in this join table rather than the Watchlist entity itself for the reason that when a user adds a movie to their Watchlist, the Date_Added field will capture that added movie, creating and representing this information for the user to view and for the database to store.

Attributes represented in the ERD:

- Watchlist_ID (Foreign Key, Integer, Not Null, references User(Watchlist ID))
- Movie_ID (Foreign Key, Integer, Not Null, References Movie(Movie_ID))
- Date_Added (Date, Not Null, Default: Current Date)

#### MovieLog

The MovieLog entity represents a list of movies that a user has already watched. Each MovieLog is tied to a unique User_ID, signifying the user who has seen these movies. This forms a mandatory-one-to-mandatory-one relationship with the User entity, as each user can log movies they have watched but a MovieLog must correspond to a user.

Each entry in the MovieLog can contain zero, one, or more Movie_IDs, each corresponding to a movie that the user has marked as watched and logged. This forms part of the optional-many-to-optional-many relationship the two entities have with each other, exactly similar to the relationship the watchlist entity have with the movie entity.

So, similar to the watchlist entity, a MovieLog can exist with zero or multiple movies, and a movie doesn't have to be in any MovieLog or can be in multiple MovieLogs. Both its functionality and implementation are similar to the watchlist entity, with the difference being its purpose.

This entity is designed to support easy logging and removal of movies as watched by a user. A user can log a movie as watched when they have seen it, and if needed, can remove it from the log.

Attributes represented in the ERD:

- MovieLog_ID (Primary Key, Integer, Not Null)
- User_ID (Foreign Key, Integer, Not Null, References User(User_ID))

##### Movielog movie association (join table)

Similar to the watchlist movie association, the MovieLog movie association table is required to help bridge the many-to-many relationship the two entities have with each other and this is done through the two foreign keys of the MovieLog_ID and Movie_ID respectively.

Additionally, a Log_date field is added in this join table rather than the MovieLog entity itself for the reason that when a user adds a movie to their MovieLog, the Log_Date field will capture that logged movie, creating and representing this information for the user to view and for the database to store.

Attributes represented in the ERD:

- MovieLog_ID (Foreign Key, Integer, Not Null)
- Movie_ID (Foreign Key, Integer, Not Null, References Movie(Movie_ID))
- Log_Date (Date, Not Null, Default: Current Date)

#### Review

The Review entity represents a user's written review and thoughts of a movie. Each review has a unique Review_ID, and contains the text of the review (Review_Text), the date the review was written (Review_Date), and the User_ID and Movie_ID of the user who wrote the review as foreign keys.

The structure of this entity enables the recording of a movie review from a user, however, for a review to exist it must at least belong to a user and a movie must belong to a review.

So the review entity relationship would read as a one-mandatory to optional-many from the user to the review entity, only because for a review to exist it must correspond to at least one user and a user is able to create zero or multiple reviews.

Now, for a review to exist, it also must be attached to at least one movie. Because it has to establish the movie the user is reviewing, that is why the relationship of the review entity to the movie entity is a optional-one to optional-many. Where a review must be connected to at least one movie but a movie can no reviews at all or multiple, and a movie can exist independently without a review.

This relationship is important to recognise and is established through the User_ID and Movie_ID which serves as foreign keys connecting the review to that specific user and the specific movie to that review.

Attributes represented in the ERD:

- Review_ID (Primary Key, Integer, Not Null)
- Review_Text (Text, Not Null)
- Review_Date (Date, Not Null, Default: Current Date)
- User_ID (Foreign Key, Integer, Not Null, References User(User_ID))
- Movie_ID (Foreign Key, Integer, Not Null, References Movie(Movie_ID))

#### Rating

The Rating entity represents a user's numerical evaluation of a movie, scored out of 5. Each rating has a unique Rating_ID and includes the score given (Rating_Score), the date the rating was made (Rating_Date), and the User_ID and Movie_ID of the user who gave the rating respectively.

Similar to the Review entity, this entity is designed to record multiple ratings by the same or different users for a single movie or multiple movies. The description of their relationship are identical to that of the Review entity.

Attributes represented in the ERD:

- Rating_ID (Primary Key, Integer, Not Null)
- Rating_Score (Integer, Not Null)
- Rating_Date (Date, Not Null, Default: Current Date)
- User_Id (Foreign Key, Integer, Not Null, References User(User_ID))
- Movie_ID (Foreign Key, Integer, Not Null, References Movie(Movie_ID))

#### Summarising the relationships

##### User to Watchlist:

- Mandatory-One-to-Mandatory-One (Each user can have one watchlist, and each watchlist must be associated with one user)

##### User to MovieLog:

- Mandatory-One-to-Mandatory-One (Each user have one movielog, and each movielog must be associated with one user)

##### User to Review:

- Mandatory-One-to-Optional-Many (Each user can write zero or multiple reviews, and each review must be associated with one user)

##### User to Rating:

- Mandatory-One-to-Optional-Many (Each user can give zero or more ratings, and each rating must be associated with one user)

##### Movie to Watchlist movie association:

- Optional-One-to-Optional-Many (Each watchlist can have zero, one or more movies, and one movie can be in a watchlist or none at all)

##### Movie to MovieLog movie association:

- Optional-One-to-Optional-Many (Each MovieLog can have zero, one or more movies, and one movie can be in a MovieLog or none at all)

##### Movie to Review:

- Optional-One-to-Optional-Many (Each movie can have zero or more reviews, and each review must be associated with at least one movie, and a movie doesn’t need to be in a review at all)

##### Movie to Rating:

- Optional-One-to-Optional-Many (Each movie can have zero or more ratings, and each rating must be associated with at least one movie, and a movie doesn’t need to be rated at all)

---

## R8: Describe your projects models in terms of the relationships they have with each other

Cinematica API employs the use of SQLAlchemy’s features as an ORM in order to represent entities as models, with each model representing classes (the entity/table itself) and instances as rows to its respective model class. The models implemented in the Cinematica API represents exactly the normalised database model as shown in the ERD.

Cinematica itself has 6 models in total, they are: `User`, `Movie`, `Watchlist`, `MovieLog`, `Review`, and `Rating`. Included and it will be discussed is the use of association tables required to bridge the many-to-many relationship that the `Watchlist` and `MovieLog` models have with the `Movie` model. Additionally, an association table was created and required to bridge the many-to-many relationship the `Watchlist` and `MovieLog` model has with each other.

### User

The `User` model represents the `users` table implemented in the database, as shown and explained with the ERD earlier, `User` acts as a main anchor point connecting and establishing the relationships with other models. All other models point towards the `User` model, since a user must exist in order for those relationships to not only be established but function as expected.

```python
class User(db.Model):
	# Table name for db
	__tablename__ = 'users'

	# Sets the user's PK
	id = db.Column(db.Integer(), primary_key=True)
	# User's email
	email = db.Column(db.String(128), nullable=False, unique=True)
	# User's username
	username = db.Column(db.String(64), nullable=False, unique=True)
	# User's password
	password = db.Column(db.String(64), nullable=False)
	# User's date joined
	join_date = db.Column(db.Date(), default=datetime.utcnow)

	# Establishing relationships:

	# Establishes one-to-one relationship with Watchlist and MovieLog models
	watchlist = db.relationship(
	'Watchlist', back_populates='user', uselist=False, cascade='all, delete')
	movielog = db.relationship(
	'MovieLog', back_populates='user', uselist=False, cascade='all, delete')
	# uselist=False changes this behaviour so it becomes one-to-one

	# Establishes one-to-many relationship with Review and Rating models
	reviews = db.relationship(
	'Review', back_populates='user', cascade='all, delete')
	ratings = db.relationship(
	'Rating', back_populates='user', cascade='all, delete')
```

The `User` model itself have a total of 4 relationships with other models, signifying its importance as the main and base model of the Cinematica API.

The relationship the `User` model has with the `Watchlist` and `MovieLog` model is a one-to-one relationship, as evidenced by the `uselist=False` parameter in the relationship function provided by SQLAlchemy. This ensures that a `User` can only have one `Watchlist` and one `MovieLog`. The `cascade='all, delete'` option ensures that if a user is deleted from the system, their associated `Watchlist` and `MovieLog` will also be removed. This prevents orphaned records in the database and helps maintain data integrity.

The other relationships the `User` model has are with the `Review` and `Rating` models. These are one-to-many relationships, meaning a single user can have multiple reviews and multiple ratings, but each review or rating can only belong to one user. This relationship is essential for functionality like tracking which users have reviewed or rated which movies. Again, the `cascade='all, delete'` option is applied to ensure that if a user is deleted, all their associated reviews and ratings are also removed.

The model attributes itself involves 5 different attributes/fields, starting with the user `id` as the main unique identifier for each user instance. With the `id` representing as primary keys which will be used to reference and connect its relationship with other models. By default SQLAlchemy sets primary keys implicitly its nullable parameter to `false`, since each `id` (PK) is required for each `user` instance is created. This is the same for its unique parameter, where it is automatically set to `true`.

The unique constraints on the `email` and `username` attributes are present in these fields to ensure that each user in the system has a distinct email and username, preventing potential conflicts and confusion in user identification. And in fact, all three, username, email, and password fields have its nullable constraint set to `false` as well, as it is required for those fields to be provided.

Lastly, the `join_date` attribute is set to default to the current date, which will automatically record when a user joins the platform.

### Movie

The `Movie` model represents the `movies` table implemented in the database, as shown and explained with the ERD earlier, similar to `User`, the `Movie` model also acts as a main anchor point connecting and establishing the relationships with other models. All other models also point towards the `Movie` model, since a movie’s information is the model instance being added and in order for the relationship to not only be established but function as expected.

```python
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

	# Establishes many-to-many relationship with Watchlist and MovieLog models

	# Note: Secondary parameter tells SQLAlchemy to use association table for handling many-to-many
	watchlists = db.relationship(
	'Watchlist', secondary=watchlist_movie_association, back_populates='movies')
	movielogs = db.relationship(
	'MovieLog', secondary=movielog_movie_association, back_populates='movies')

	# Establishes one-to-many relationship with Review and Rating models
	reviews = db.relationship('Review', back_populates='movie')
	ratings = db.relationship('Rating', back_populates='movie')
```

The `Movie` model also has a total of 4 relationships with other models, reflecting its central role within the Cinematica API.

Starting with its many-to-many relationships, the `Movie` model connects with both the `Watchlist` and `MovieLog` models. These relationships are connected using association tables, `watchlist_movie_association` and `movielog_movie_association`, as indicated by the `secondary` parameter in the relationship function. This means that a single movie can be part of numerous watchlists and movie logs, while a single watchlist or movie log can contain multiple movies.

The `back_populates` attribute enables a bidirectional relationship, granting ease of access from either end. In other words, one Movie can be part of many `Watchlists`/`MovieLogs` and vice versa. Therefore, from the Movie's perspective, it "has many" `Watchlists` and `MovieLogs`, hence the plural `watchlists` and `movielogs`.

Moving to the one-to-many relationships, the `Movie` model interacts with the `Review` and `Rating` models. In this relationship, one movie can accumulate multiple reviews and ratings. However, each specific review or rating is exclusively linked to one individual movie. The `back_populates` attribute in these relationships ensures bidirectional access, meaning from the Movie's perspective, it "has many" Reviews and Ratings, hence the plural `reviews` and `ratings`.

Additionally, essential attributes like `title`, `director`, `genre`, `runtime`, and `release_year` ensure that comprehensive details about a movie are available in the system. The non-null constraints (`nullable=False`) on these fields emphasise the necessity of these details for every movie entry, ensuring a consistent dataset.

### Watchlist

The `Watchlist` model represents the `watchlists` table implemented in the database, as shown and explained with the ERD, it serves as a way for users to add movies to their `watchlist` collection so they are able to store and track which movies they wish to watch in the future.

```python
class Watchlist(db.Model):
	# Table name for db
	__tablename__ = 'watchlists'

	# PK for each movie entry in the watchlist
	id = db.Column(db.Integer(), primary_key=True)
	# FK for user
	# unique parameter set to True to enforce one-to-one relation
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

	# Establishing relationships:

	# Establishes (one-to-one) relationship with user
	user = db.relationship('User', back_populates='watchlist')

	# Establishes many-to-many relationship with Movie model through association table
	movies = db.relationship('Movie', secondary=watchlist_movie_association, back_populates='watchlists')
```

Starting with the one-to-one relationship with the `User` model, every `Watchlist` is tied to a unique user. This relationship is evidenced by the `unique=True` constraint on the `user_id` attribute, which is a foreign key referencing the `users` table. By setting this constraint, it ensures that each user can have only one watchlist and vice-versa. This singular bond between a user and their watchlist is further reinforced by the bidirectional relationship attribute, `back_populates`, enabling the connection between a user and their associated watchlist.

Shifting focus to the many-to-many relationship with the `Movie` model, the relationship the `Watchlist` model has with the `Movie` model as we saw earlier is connected through an association table, `watchlist_movie_association`, to facilitate this many-to-many relationship.

```python
watchlist_movie_association = db.Table('watchlist_movie_association',
	db.Column('watchlist_id', db.Integer, db.ForeignKey(
	'watchlists.id'), primary_key=True),
	db.Column('movie_id', db.Integer, db.ForeignKey(
	'movies.id'), primary_key=True),
	db.Column('date_added', db.Date(),
	nullable=False, default=datetime.utcnow)
)
```

This table effectively bridges the `Watchlist` and `Movie` models, allowing multiple movies to be associated with a single watchlist and, also for a single movie to be present in multiple users' watchlists. This ensures that users can add as many movies as they desire to their watchlist without any constraints.

Both the `watchlist_id` and `movie_id` are present in the `watchlist_movie_association` table as attributes and more importantly as foreign keys which of course links back its respective movie and the watchlist it belongs to. Now, notice the `primary_key=True` parameter present in these two foreign keys, they essentially make up the compound primary key for the `watchlist_movie_association` table. This means that the combination of a particular `watchlist_id` and `movie_id` is unique and ensures that the same movie cannot be added more than once to the same watchlist. In essence, this design enforces a uniqueness constraint on pairs of watchlists and movies, providing data integrity by preventing duplicate entries within a user's watchlist.

Additionally, the table incorporates a `date_added` attribute, which records the date when a specific movie is added to a watchlist. This can be especially useful for sorting and retrieving movies based on when they were added to the watchlist, giving users the ability to see their most recent additions. The `nullable=False` ensures that every movie added to a watchlist will always have a date associated with it, and the `default=datetime.utcnow` automatically stamps the current date and time when a new association is created.

Again, the `back_populates` attribute in the `Watchlist` model ensures mutual access which references the `watchlists` attribute in the `Movie` model, allowing for a watchlist's movies to be queried and vice-versa. This is what backpopulates does, its required in SQLAlchemy that the relationship is symmetrically mirrored. When you have a relationship in one model pointing to another, the `back_populates` attribute ensures that the relationship is also accessible from the other side, creating a two-way synchronization of data.

For instance, when you access the `movies` attribute of a `Watchlist` instance, SQLAlchemy knows to look at the associated movies for that particular watchlist. Similarly, when you access the `watchlists` attribute of a `Movie` instance, SQLAlchemy knows to fetch all the watchlists where that movie exists.

This bidirectional behavior is particularly powerful for querying, updating, and maintaining relationships in the database. It simplifies operations by offering intuitive ways to access related data and maintains data integrity by ensuring consistency between the two related sides.

The `back_populates` parameter ensures that relationships between models are dynamic, interconnected, and responsive, making it easier for developers to work with the ORM and providing users with consistent and coherent data across entities.

### MovieLog

The `MovieLog` model represents the `movielogs` table implemented in the database, as shown and explained with the ERD, it serves as a way for users to add movies to their `movielog` collection so they are able to store and track which movies they have already watched.

```python
class MovieLog(db.Model):
	# Table name for db
	__tablename__ = 'movielogs'

	# PK for each movie entry in the movie log
	id = db.Column(db.Integer(), primary_key=True)
	# FK for user
	# unique parameter set to True to enforce one-to-one relation
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

	# Establishing relationships:

	# Establishes (one-to-one) relationship with user
	user = db.relationship('User', back_populates='movielog')

	# Establishes many-to-many relationship with Movie model through association table
	movies = db.relationship('Movie', secondary=movielog_movie_association, back_populates='movielogs')
```

Beginning with the one-to-one relationship with the `User` model, every `MovieLog` is associated with a distinct user. This connection is define by the `unique=True` constraint on the `user_id` attribute, acting as a foreign key pointing to the `users` table. This constraint guarantees that each user can have only one movielog and vice-versa. The bond between a user and their movielog is further emphasized through the bidirectional relationship attribute, `back_populates`, which facilitates the linkage between a user and their respective movielog.

Transitioning to the many-to-many relationship with the `Movie` model, similar to the `Watchlist` model, the bond the `MovieLog` model shares with the `Movie` model is also connected via the association table `movielog_movie_association`.

```python
movielog_movie_association = db.Table('movielog_movie_association', db.Column('movielog_id', db.Integer, db.ForeignKey('movielogs.id'), primary_key=True),
db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
db.Column('date_logged', db.Date(), nullable=False, default=datetime.utcnow))
```

This table essentially bridges the `MovieLog` and `Movie` models, allowing multiple movies to be affiliated with a singular movielog while also allowing a single movie to appear in various users' movielogs. It ensures users can log as many movies as they wish in their movielog.

Both the `movielog_id` and `movie_id` serve as crucial foreign keys within the `movielog_movie_association` table, linking them back to their respective movie and movielog. The `primary_key=True` parameter in these two columns forms the compound primary key for the table. This design means that the `movielog_id` and `movie_id` is distinct and unique, ensuring a movie isn't logged more than once in the same movielog. Essentially, this helps with data integrity by avoiding repetitive entries within a user's movielog.

The table features a `date_logged` attribute, capturing the moment a user logs a movie. This attribute is important for organising and accessing movies based on their logging dates, granting users insight into their most recent film experiences. The `nullable=False` assures that every movie logged will always have an associated date, and the `default=datetime.utcnow` ensures the present date and time are automatically noted when a new entry is made.

The `back_populates` attribute in the `MovieLog` model guarantees access and connection, referring to the `movielogs` attribute in the `Movie` model. This ensures movies within a specific movielog can be queried and vice-versa. The magic of backpopulates shows that relationships in SQLAlchemy are symmetrically reflected. It means if there's a relationship in one model pointing to another, the relationship should be reachable from the opposing side, forging a dual-way data synchronisation.

### Review

The `Review` model represents the `reviews` table implemented in the database, as shown and explained with the ERD, it serves as a way for users to add reviews of movies they have written and add to their `reviews` collection so they are able to store and track which movies they have reviewed.

```python
class Review(db.Model):
	# Table name for db
	__tablename__ = 'reviews'

	# PK for each movie review
	id = db.Column(db.Integer(), primary_key=True)
	# Body text of movie review
	review_text = db.Column(db.Text(), nullable=False)
	# The movie review's date
	review_date = db.Column(
	db.Date(), nullable=False, default=datetime.utcnow)
	# Fk for user
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	# FK for movie
	movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

	# Establishing relationships:

	# Establishing relationship with User and Movie
	user = db.relationship('User', back_populates='reviews')
	movie = db.relationship('Movie', back_populates='reviews')
```

The `Review` model sets up two significant relationships, marking its position as a central space for user thoughts within the Cinematica API.

It directly aligns itself with the `User` model, establishing that a single user can write many reviews. Yet, every unique review, belongs to exactly one user. The `back_populates` attribute solidifies this bond, allowing two-way access. Viewed from the Review's lens, where each review "belongs to" one specific `User`.

Similarly, the `Review` model creates a bridge to the `Movie` model. Here, one movie can have many reviews, from the many different users. Still, each review is tailored for one specific movie. The `back_populates` attribute plays its role here too, facilitating access from both ends. For a `Review`, it uniquely "belongs to" one `Movie`.

The are two foreign keys in the `Review` model, the `user_id` and `movie_id`.These foreign keys ensure that every review is decisively linked to both a user and a movie. This system reinforces that no review is ever orphaned or misplaced.

Attributes like `review_text` and `review_date` are important information to the `Review` model, as they provide the text of the review itself and also the date when the movie is reviewed. The non-null constraints (`nullable=False`) ensures a review entry is provided every single time.

### Rating

The `Rating` model represents the `ratings` table implemented in the database, as shown and explained with the ERD, it serves as a way for users to add ratings of movies they have watched and add to their `ratings` collection so they are able to store and track which movies they have rated.

```python
class Rating(db.Model):
	# Table name for db
	__tablename__ = 'ratings'

	# PK for ratings
	id = db.Column(db.Integer(), primary_key=True)
	# Holds the movies score rating
	rating_score = db.Column(db.Integer(), nullable=False)
	# The date the movie is rated
	rating_date = db.Column(db.Date(), nullable=False, default=datetime.utcnow)

	# Fk for user
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	# FK for movie
	movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

	# Establishing relationships:

	# Establishing relationship with User and Movie
	user = db.relationship('User', back_populates='ratings')
	movie = db.relationship('Movie', back_populates='ratings')
```

Just as the `Review` model connects with the `User` model, the `Rating` model does too, indicating that one user can have multiple ratings, but each specific rating is attributed to only one user. The `back_populates` attribute is again at play, allowing access from both ends. From the perspective of the `Rating`, each rating "belongs to" a single `User`.

The connection between the `Rating` model and the `Movie` model is also mirrored from the `Review` model. This means that one movie can have multiple ratings. Still, every individual rating is tailored for a specific movie. The `back_populates` parameter facilitates two-way access between these models, ensuring that each `Rating` is uniquely linked to a specific `Movie`.

We again see the presence of the foreign keys, `user_id` and `movie_id`, in the `Rating` model. These keys make sure every rating is associated with a user and a movie.

The `rating_score` and `rating_date` attributes bring the core information to the `Rating` model. While `rating_score` provides the numerical value of the user's feedback, `rating_date` notes when the movie was rated. The non-null requirements (`nullable=False`) on these fields make sure every rating entry is complete and provided.

---

## R7: Detail any third party services that your app will use

Cinematica was built entirely using Python with Flask as the chosen web app framework, its the perfect choice for this MVC version of Cinematica. Flask allows developers to build web app’s fairly efficiently, its lightweight and flexible framework and architecture allows Flask to adapt to a number of application design patterns and architectural styles such as the MVC architecture.

Adopting the MVC architecture, Cinematica is utilising the model and controller aspect of the paradigm when using Flask to develop the RESTful API. With the view aspect embedded in the controller itself, responding to the client with information in JSON format.

Flask allows for the extension of its functionality through third-party services and packages makes it a great choice for smaller projects and services such as this RESTful API. Flask handles scalability quite well, which is perfect for the set of features and components that the Cinematica API hopes to implement in the future.

Extending Flask through its third party services allows Flask to provide a powerful workflow that involves database interaction and access through an ORM, serialisation & deserialisation of data, authentication & authorisation and encryption security features just to name a few. On that note, here are some of the third-party services used to build the Cinematica API alongside Flask:

### SQLAlchemy/Flask-SQLAlchemy

SQLAlchemy is a widely-used Object Relational Mapper (ORM) for many Python developers. What makes it stand out is its ability to let developers interact with databases like they're working with Python objects. This essentially provides an abstraction layer through Python OOP concepts, with SQLAlchemy representing database tables as classes and table rows as instances of those class tables.

This means no more writing tedious SQL queries for basic tasks; SQLAlchemy takes care of that. The Flask-SQLAlchemy extension makes for a much more seamless experience for Flask developers. It provides a set of tools that integrates SQLAlchemy right into a Flask app, making database tasks feel like just another part of the app.

When we talk about databases, PostgreSQL is the one chosen for Cinematica API. It's reliable, fast, and works well with SQLAlchemy. What this means for the Cinematica API is that any interactions with the database, from fetching a movie's details to updating a user's watchlist, happens smoothly. SQLAlchemy takes care of turning high-level commands into efficient SQL, with this, Cinematica can operate on its underlying data without having to delve into raw SQL, allowing for more maintainable and secure database interactions.

### Psycopg2

Psycopg2 is a PostgreSQL adapter for Python. Since Cinematica uses PostgreSQL as its primary data storage solution due to its robustness, reliability, and scalability. Psycopg2 acts as a bridge between the application and the PostgreSQL server, ensuring smooth and efficient data transactions. It supports various PostgreSQL features such as performing the full CRUD operations extending and abstracting SQL queries through SQLAlchemy and can handle large volumes of data, making it a vital tool for the Cinematica API's data handling needs.

### Marshmallow/Flask-Marshmallow

Marshmallow is a library for object serialization/deserialization, turning complex data types, such as objects, into a format that can be easily rendered into JSON. Marshmallow helps validate any incoming/input data into the server by checking certain validations established through a schema (a template/blueprint of sorts). Marshmallow schema’s not only helps validate data, but it helps in converting it through serialisation when responding back to the client and deserialisation when receiving data as a request to the server into its appropriate data type in the form of objects.

Flask-Marshmallow is an integration layer for Flask and Marshmallow which makes it easier to use with a Flask application. For Cinematica, this means simpler transformations between the ORM models and the JSON responses sent to the client, in other words the schema itself communicates with the appropriate database models, ensuring data integrity and consistency.

### Python-Dotenv

Environment variables are crucial for protecting sensitive information and configuration settings. Python-Dotenv enables Cinematica to load environment variables from a `.env` file into the Flask configuration. This aids in keeping the application's sensitive information, like database credentials and secret keys, out of the codebase, ensuring security and ease of configuration.

By separating the concerns of sensitive information and credentials into its own `.env` file, it extends the modular aspect of the Flask application and its various configuration methods. That means that different developers working on the application might have unique environment variables created based on their personal or system preferences.

### JWT/Flask-JWT-Extended

JWT (JSON Web Tokens) is a compact and self-contained method for safely transmitting information between parties as a JSON object. Flask-JWT-Extended extends the capabilities of JWT to Flask applications, providing a robust solution for user authentication and authorization. For Cinematica, this means user sessions and data requests are securely managed and verified, ensuring only authenticated users can access certain endpoints.

Whenever a user either registers or logs in to the Cinematica API, they will receive the JWT access token required to access certain endpoints throughout the API. In this current MVC version of the API, the token itself has to be included in the authorisation header as a bearer token. The token provided by JWT will authenticate that the user is a valid user of the Cinematica API, and also authorise users from accessing certain endpoints and preventing users from otherwise unauthorised endpoints all in keeping the safety, privacy and integrity of the information stored in Cinematica.

### Bcrypt/Flask-Bcrypt

Security is paramount, especially when dealing with user passwords. Bcrypt is a popular password-hashing algorithm. Flask-Bcrypt provides Bcrypt hashing utilities for a Flask application. With this, Cinematica ensures that user passwords are securely hashed and ancrypted before being stored in the database, safeguarding user data against potential breaches.

Bcrypt hashes users passwords both in the database/server level and also in any form of interactions and transactions made between the client and the server, so neither the developers themselves, yet alone bad actors will have access to the original raw password, only the hashed password. Only the user will see their password when inputting in the client side, which automatically gets hashed when that (log in as an example) request is sent to the server.

### Postman

Postman is an API testing and development tool, allowing developers to send requests to and receive responses from APIs. During the development of Cinematica, Postman played a crucial role in testing and validating the API endpoints. With its intuitive user interface and extensive feature set, it ensured that the Cinematica API functions as intended, providing reliable and consistent results.

---

## R10: Describe the way tasks are allocated and tracked in your project

### Initial & pre-development planning

Cinematica API was first initially drafted based on my enthusiasm for movies in general but also being a fan of the social movie review/rating platform Letterboxd, this is something I was curious in tackling at with of course a much smaller scale working with movie data but also have the social aspect of being able to see other users movie reviews and ratings.

Planning started with quickly drafting which entities was required to make up the overall structure that would shape the database schema and its design. Initially, I quickly drafted my initial ideas and presented these for feedback which the idea for the API itself was required for it to be approved before development can begin.

We used Discord to present our ideas, and here is a screenshot of my initial idea:

<img src="./docs/Screenshots/disc.jpg" width="250"></img>

Shortly after, I presented a draft of the ERD for the Cinematica API, it being one of many iterations. Here is the the image of the first draft:

<img src="./docs/Movie-API-ERD_V1.jpg"></img>

If you wish to view other iterations of the Cinemetica API ERD, please find them [*here*](https://github.com/jordansbenjamin/Cinematica_API/blob/main/docs/ERD-iterations.md).

During this initial planning phase, there was some back and forth between the educators and myself when discussing feedbacks on the drafted ideas and potential directions for the API, here are some examples of those discussions:

<img src="./docs/Screenshots/disc2.jpg" width="250"></img>

<img src="./docs/Screenshots/disc3.jpg" width="250"></img>

<img src="./docs/Screenshots/disc4.jpg" width="250"></img>

<img src="./docs/Screenshots/disc5.jpg" width="250"></img>

### Development

The planning phase for the API was then brought on to Trello, which is the tracking and project management tool I used for this project. This is straight after the approval of the ERD for the Cinematica API. Allowing me to start working on pre-development planning.

I added all the tasks required each step of the way from the initial planning phase, all the way to the development phase and even post-development where I’m writing the documentation as I write this to Trello.

You can find the Trello board I used for the Cinematica API project here: [Cinematica-API_Trello-Board](https://trello.com/b/3938cdC4/cinematica-api)

<img src="./docs/Screenshots/trello.jpg" width="450"></img>

I separated the Trello board into 5 different parts using the Trello list feature, they are separated and named as follows:

**Extra/Nice to have:**

- This list contains cards with a bunch of features I hope to development if there is enough time, which it turns out a majority of them I unfortunately was not able to implement.
- The cards are signified with an indigo cover, additionally with a label which is labelled (no pun intended) as ‘Extra’ (in indigo colour as well).

**Documentation to do:**

- This list contains cards with documentation tasks that are required to be completed for the project, separating the documentation tasks helps in organising the project as documentation was a good chunk of the project itself.
- The cards are signified with a blue cover, additionally it utilises three different labels which depending on the individual tasks themselves can fall under the category of ‘Planning’ (yellow), ‘Docs’ (blue), ‘Development’ (green), and ‘Post Development’ (red).

**Development to do:**

- This list contains cards with tasks related to development, from initial set up to coding and debugging, and even tasks related to post development such as bash scripting belongs in this list.
- The cards themselves have 3 different covers which signifies the 3 phases of development, from planning (yellow), development (green) and post development (red). The labels reflect exactly these as well for each card.

**Active:**

- The active list simply stores any active tasks for easier identification of the tasks that needs to be accomplished.

**Finished:**

- Lastly, the finished list contains all completed tasks/cards for the project.

**Other things to note using Trello for the Cinematica API project:**

- With each card I added a due date to keep track of the tasks that needs to be done and especially on time. It also has a 1 day reminder for all due dates.
- I also used a checklist for the required tasks/cards, which is especially helpful in breaking down the tasks that needs to be done.
- The Trello board changed slightly over the course of the project, some screenshots I provided are probably from the earlier phase of the project, and I thought it would be good to include that to see how the changes are reflected overtime.

**Here are some screenshots of selected cards:**

<img src="./docs/Screenshots/trello2.jpg" width="400"></img>

<img src="./docs/Screenshots/trello3.jpg" width="400"></img>

<img src="./docs/Screenshots/trello4.jpg" width="400"></img>

You will notice that I broke down some of the larger components when tackling the project into its own individual cards, for example the controller, model, and schema cards are separated into their own sections with checklists of their own.

However, some tasks overlaps, such as the validation required for the project are added into the schemas cards as they are closely related to each other. More importantly, the development process itself was not as linear as I hope it to be, but I’m quickly learning that must be part of the process. Despite trying my best to stick with the tasks at hand as defined with each Trello card.

But, for example, I learned that sometimes while debugging, you often find new ways to implement a certain component and often you do get sidetracked from the main task at hand because it requires you to tackle other features that was originally planned for later stages in the development cycle. But overall, this was a challenging but quite fun project to tackle, learned more that I could imagine

As a final reminder and for convenience, please visit the [*Trello board*](https://trello.com/b/3938cdC4/cinematica-api) to have a look at it more in depth.

---

## References

Dhruv, S. (2019). Pros and Cons of using PostgreSQL for Application Development. [online] Aalpha. Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/.

‌Pedamkar, P. (2019). What is PostgreSQL? | Features | Advantages and Disadvantages. [online] EDUCBA. Available at: https://www.educba.com/what-is-postgresql/.

‌author (2022). PostgreSQL Tutorials | What is PostgreSQL, Advantages, Disadvantages. [online] < Code Topology />. Available at: https://codetopology.com/database/what-is-postgresql/.

‌Auth0 - Blog. (n.d.). SQLAlchemy ORM Tutorial for Python Developers. [online] Available at: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/.

‌Fullstackpython.com. (2012). SQLAlchemy. [online] Available at: https://www.fullstackpython.com/sqlalchemy.html.

‌Abba, I.V. (2022). What is an ORM – The Meaning of Object Relational Mapping Database Tools. [online] freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/.

‌DEV Community 👩‍💻👨‍💻. (n.d.). Why we should always use ORM? [online] Available at: https://dev.to/anubhavitis/why-we-should-always-use-django-orm-2l6m.

‌DEV Community. (2020). Flask with SQLAlchemy & Marshmallow. [online] Available at: https://dev.to/nahidsaikat/flask-with-sqlalchemy-marshmallow-5aj2 [Accessed 12 Aug. 2023].

‌nordvpn.com. (2023). What is bcrypt and how does it work? | NordVPN. [online] Available at: https://nordvpn.com/blog/what-is-bcrypt/.

‌4Geeks. (n.d.). Understanding JWT and how to implement a simple JWT with Flask. [online] Available at: https://4geeks.com/lesson/what-is-JWT-and-how-to-implement-with-Flask [Accessed 12 Aug. 2023].

‌
