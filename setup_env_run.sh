# #!/bin/bash

# # Check Python version and existence
# check_python(){
#     if ! [[ -x "$(command -v python3)" ]]; then
#         echo "Error: 
#             Python 3 is required for Cinematica API.
#             Please install the latest version of Python 3 from: https://www.python.org/downloads/installing-python/" >&2
#         exit 1
#     fi
# }

# # Creates virtual environment
# create_virtual_venv(){
#     if [ -d "src/$1" ]; then
#         echo "A virtual environment named $1 already exists in the src directory!"
#         echo "Skipping virtual environment creation."
#     else
#         python3 -m venv src/$1
#         echo "Virtual environment $1 created in the src directory!"
#     fi
# }

# # Activates virtual environment
# activate_virtual_venv(){
#     source src/$1/bin/activate
# }

# # Upgrades to the latest version of pip
# upgrade_pip(){
#     pip install --upgrade pip
# }

# # Install requirements and dependencies
# install_requirements(){
#     pip install -r $1  
# }

# # Create .env file with required environment variables
# create_env_file(){
#     cat <<EOT >> src/.env
# DATABASE_URL="postgresql+psycopg2://cinematica_dbuser:cinematica888@localhost:5432/cinematica_db"
# SECRET_KEY="the_most_secret_key"
# EOT
# }

# # Resets the database before running the API
# reset_database(){
#     pushd src
#     flask db drop
#     flask db create
#     flask db seed
#     echo "Database reset complete!"
#     popd
# }


# # Main execution of bash script
# echo "Welcome! Let's get you set up for Cinematica API!"

# sleep 2
# clear

# check_python

# create_virtual_venv .venv

# activate_virtual_venv .venv
# echo "Virtual environment created and activated in the src directory!"

# sleep 2

# upgrade_pip
# clear

# install_requirements src/requirements.txt

# create_env_file

# echo "Requirements and dependencies installed. .env file created in src directory!"

# sleep 2
# clear

# reset_database

# sleep 2
# clear

# echo "Setup complete! Virtual environment initialised, dependencies installed. To start the Cinematica API, navigate to the src folder and run: 'flask run'"

# flask run

#!/bin/bash

# Check Python version and existence
check_python(){
    if ! [[ -x "$(command -v python3)" ]]; then
        echo "Error: 
            Python 3 is required for Cinematica API.
            Please install the latest version of Python 3 from: https://www.python.org/downloads/installing-python/" >&2
        exit 1
    fi
}

# Creates virtual environment
create_virtual_venv(){
    if [ -d "$1" ]; then
        echo "A virtual environment named $1 already exists in the src directory!"
        echo "Skipping virtual environment creation."
    else
        python3 -m venv $1
        echo "Virtual environment $1 created in the src directory!"
    fi
}

# Activates virtual environment
activate_virtual_venv(){
    source $1/bin/activate
}

# Upgrades to the latest version of pip
upgrade_pip(){
    pip install --upgrade pip
}

# Install requirements and dependencies
install_requirements(){
    pip install -r $1  
}

# Create .env file with required environment variables
create_env_file(){
    cat <<EOT >> .env
DATABASE_URL="postgresql+psycopg2://cinematica_dbuser:cinematica888@localhost:5432/cinematica_db"
SECRET_KEY="the_most_secret_key"
EOT
}

# Resets the database before running the API
reset_database(){
    flask db drop
    flask db create
    flask db seed
    echo "Database reset complete!"
}


# Main execution of bash script
echo "Welcome! Let's get you set up for Cinematica API!"

sleep 2
clear

check_python

create_virtual_venv .venv

activate_virtual_venv .venv
echo "Virtual environment created and activated in the src directory!"

# Change to the src directory
cd src

sleep 2

upgrade_pip
clear

install_requirements requirements.txt

create_env_file

echo "Requirements and dependencies installed. .env file created!"

sleep 2
clear

reset_database

sleep 2
clear

echo "Setup complete! Virtual environment initialised, dependencies installed. Starting the Cinematica API now..."

flask run
