from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_db_host():
    """
    Get the database host from environment variables.
    """
    return os.getenv("MYSQL_HOST")

def get_db_user():
    """
    Get the database user from environment variables.
    """
    return os.getenv("MYSQL_USER")

def get_db_password():
    """
    Get the database password from environment variables.
    """
    return os.getenv("MYSQL_PASSWORD")

def get_db_name():
    """
    Get the database name from environment variables.
    """
    return os.getenv("MYSQL_DATABASE")