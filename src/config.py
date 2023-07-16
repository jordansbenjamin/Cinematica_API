import os


# Define a configuration class
class Config(object):
    # Turn off SQLAlchemy's event system, which can consume a lot of resources.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Fetch the secret key for JWT from environment variables.
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")

    # Define a property that retrieves the database URL from environment variables.
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DATABASE_URL")
        # If the DATABASE_URL variable is not set, raise an error.
        if not value:
            raise ValueError("DATABASE_URL is not set")
        # If it is set, return the value.
        return value


# A configuration specific to the development environment.
class DevelopmentConfig(Config):
    # Enable debug mode in development.
    DEBUG = True


# A configuration specific to the production environment.
class ProductionConfig(Config):
    # No specific configurations for now.
    pass


# A configuration specific to the testing environment.
class TestingConfig(Config):
    # Enable testing mode.
    TESTING = True


# Fetch the current environment from environment variables.
environment = os.environ.get("FLASK_ENV")

# Depending on the current environment, use a different configuration.
if environment == "production":
    # If the environment is production, use the production configuration.
    app_config = ProductionConfig()
elif environment == "testing":
    # If the environment is testing, use the testing configuration.
    app_config = TestingConfig()
else:
    # If the environment is neither production nor testing, use the development configuration.
    app_config = DevelopmentConfig()
