from dotenv import load_dotenv
import os
import json

def get_polygon_api_key() -> str:
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("POLYGON_API_KEY")

    if not api_key:
        raise ValueError("POLYGON_API_KEY is not set. Please add it to your .env file.")
    
    return api_key

def get_xtb_credentials(username: str) -> dict:
    """
    Retrieve username and password for a given personal name from the environment variables.

    Args:
        username (str): The username associated with the credentials.

    Returns:
        dict: A dictionary containing 'email' and 'password'.

    Raises:
        ValueError: If the credentials are not found or are not properly formatted.
    """
    # Load environment variables
    load_dotenv()
    credentials_json = os.getenv("XTB_CREDENTIALS")
    
    if not credentials_json:
        raise ValueError("`XTB_CREDENTIALS` is not set. Please add it to your .env file.")

    try:
        credentials = json.loads(credentials_json)
    except json.JSONDecodeError:
        raise ValueError("`XTB_CREDENTIALS` is not a valid JSON string.")

    for entry in credentials:
        if entry["username"] == username:
            return entry['credentials']
    
    raise ValueError(f"Credentials for '{username}' not found.")