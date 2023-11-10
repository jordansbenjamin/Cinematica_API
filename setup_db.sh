#!/bin/bash

# Check PostgreSQL installation
check_postgresql(){
    if ! [[ -x "$(command -v psql)" ]]; then
        echo "Error:
            PostgreSQL is required to set up the Cinematica database.
            Please install PostgreSQL. Refer to: https://www.postgresql.org/download/"
        exit 1
    fi
}

# Check if the database already exists
check_database_exists(){
    if psql -lqt | cut -d \| -f 1 | grep -qw cinematica_db; then
        echo "Database 'cinematica_db' already exists. Skipping database creation."
        exit 1
    fi
}

# Create the database and user, grant privileges
setup_database(){
    psql << EOF
        CREATE DATABASE cinematica_db;
        CREATE USER cinematica_dbuser WITH PASSWORD 'cinematica888';
        GRANT ALL PRIVILEGES ON DATABASE cinematica_db TO cinematica_dbuser;
EOF
}

# Main execution of bash script
echo "Welcome! Let's get you set up with the Cinematica database!"

sleep 2
clear

check_postgresql
check_database_exists
setup_database

echo "Database 'cinematica_db' has been created, user 'cinematica_dbuser' set up, and privileges granted!"