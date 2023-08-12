# Cinematica API

A RESTful API for movie enthusiasts to review, rate and keep track of movies throughout their cinematic journey.

This project is developed as an assignment for Coder Academy, it being an API webserver, there is no front-end implemented. To test the functionality of the API, you can use API client testing tools such as Postman or Insomnia to have a UI to test the API endpoints on.

Otherwise you can view via JSON on a webpage?

---

## Installation Guide

### System Requirements

To start testing the API, since it was developed and built on Python. It is a requirement that **Python 3** is installed on your computer.

You can check which version of python is installed or if you have it installed at all by:

#### Checking version of Python in the Terminal / shell

1. Depending on your operating systems, there are different ways to open the terminal/shell:

- For Macintosh `CMD + space` to open spotlight, then simply type in ***terminal***
- For Windows `Windows key + x` then select ***command prompt***. Followed by typing `bash` in the command prompt.

For both operating systems, type:

```shell
python --version
```

If you don't have Python 3 already installed, please follow visit this [*website*](https://realpython.com/installing-python/) for steps on installing Python 3 to your device and operating system of choice.

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

Before continuing with the installlation process, please make sure PostreSQL is installed. You can find and download PostgreSQL for your device and operating system [*here*](https://www.postgresql.org/download/).

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

4. After that, type these two commands ***separately*** to allow permission for executing the Blackjack program:

```shell
chmod +x setup_db.sh
```

```shell
chmod +x setup_env.sh
```

5. To get you set up before running the Cinematica API program, the PostgreSQL database needs to be set up, thankfully, all you need to do is run the bash script command here:

```shell
./setup_db.sh
```

6. After the database is setup, you need to install some requirements, dependencies, and also setting up the environment variables required to run the program:

```shell
./setup_env_run.sh
```

This bash script will also automatically activate the virutal environment required to run the program but also run the program itself.

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