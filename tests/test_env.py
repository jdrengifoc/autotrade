import unittest
import pytest
from autotrade.utils import get_polygon_api_key

@pytest.mark.env
class TestAPIKeyLoading(unittest.TestCase):

    def test_api_key_loaded(self):
        POLYGON_API_KEY = get_polygon_api_key()
        
        # Ensure that the API key is loaded and is not None or empty.
        self.assertIsNotNone(POLYGON_API_KEY, "POLYGON_API_KEY is not set in the environment")
        self.assertNotEqual(POLYGON_API_KEY, "", "POLYGON_API_KEY is empty")