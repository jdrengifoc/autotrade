from dotenv import load_dotenv
import os
import requests

def get_polygon_api_key() -> str:
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("POLYGON_API_KEY")

    if not api_key:
        raise ValueError("POLYGON_API_KEY is not set. Please add it to your .env file.")
    
    return api_key

def check_ticker_available(ticker: str) -> bool:
    API_KEY = get_polygon_api_key()
    url = f"https://api.polygon.io/v3/reference/tickers/{ticker}"
    
    # Make the API request
    response = requests.get(url, params={"apiKey": API_KEY})
    
    # Check if the response is successful
    if response.status_code == 200:
        # If successful, return True indicating the ticker exists
        return True
    elif response.status_code == 404:
        # If not found (404), return False indicating the ticker does not exist
        return False
    else:
        # For any other errors, raise an exception
        response.raise_for_status()