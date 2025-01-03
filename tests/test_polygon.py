import pytest
from autotrade.utils import get_polygon_api_key
from polygon import RESTClient

@pytest.mark.polygon
def test_polygon_client():
    
    # Initialize the Polygon REST client
    client = RESTClient(api_key=get_polygon_api_key())

    # Example API call: Get details of a specific stock ticker
    ticker = "AAPL"  # Apple Inc.
    response = client.get_ticker_details(ticker)
    
    # Check if the response contains expected keys
    assert response, "Response is empty or None."
    assert hasattr(response, "ticker"), "Ticker not found in response."
    assert response.ticker == ticker, f"Expected ticker {ticker}, got {response['ticker']}."
