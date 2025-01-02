import unittest
import os
from dotenv import load_dotenv
import pytest

# Mark this module as "environment-related" tests
@pytest.mark.env
class TestAPIKeyLoading(unittest.TestCase):

    def setUp(self):
        # Load environment variables from .env file
        load_dotenv()

    def test_api_key_loaded(self):
        # Check if the API key is loaded from the environment
        POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
        print(POLYGON_API_KEY)
        # Ensure that the API key is loaded and is not None or empty
        self.assertIsNotNone(POLYGON_API_KEY, "POLYGON_API_KEY is not set in the environment")
        self.assertNotEqual(POLYGON_API_KEY, "", "POLYGON_API_KEY is empty")

    def test_missing_api_key(self):
        # Ensure that if the API key is missing, a ValueError is raised
        POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

        if not POLYGON_API_KEY:
            raise ValueError("POLYGON_API_KEY is not set. Please add it to your .env file.")
