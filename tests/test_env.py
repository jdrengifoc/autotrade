import unittest
from unittest.mock import patch
import pytest
import os
import json
from autotrade.utils import get_polygon_api_key, get_xtb_credentials

@pytest.mark.env
class TestPOLYGON_APIKeyLoading(unittest.TestCase):

    def test_api_key_loaded(self):
        POLYGON_API_KEY = get_polygon_api_key()
        
        # Ensure that the API key is loaded and is not None or empty.
        self.assertIsNotNone(POLYGON_API_KEY, "POLYGON_API_KEY is not set in the environment")
        self.assertNotEqual(POLYGON_API_KEY, "", "POLYGON_API_KEY is empty")


@pytest.mark.env
class TestXTB_Credentials(unittest.TestCase):

    def setUp(self):
        """Set up the environment variable for the tests."""
        # You can set up the mock value here
        self.valid_credentials = [
            {"username": "JohnDoe", "credentials": {"email": "johndoe_email", "password": "johndoe_password"}},
            {"username": "JaneSmith", "credentials": {"email": "janesmith_email", "password": "janesmith_password"}}
        ]

    def test_xtb_credentials_loaded(self):
        """Test that the XTB credentials are correctly loaded from the environment."""
        # Set the environment variable for testing purposes
        os.environ["XTB_CREDENTIALS"] = json.dumps(self.valid_credentials)
        
        credentials = get_xtb_credentials("JohnDoe")

        self.assertEqual(credentials, {"email": "johndoe_email", "password": "johndoe_password"},
                         "The credentials for JohnDoe do not match.")

    def test_xtb_credentials_invalid_json(self):
        """Test that a ValueError is raised if the XTB_CREDENTIALS variable contains invalid JSON."""
        # Set an invalid JSON string
        os.environ["XTB_CREDENTIALS"] = "invalid_json"

        with self.assertRaises(ValueError) as context:
            get_xtb_credentials("JohnDoe")
        
        self.assertTrue("`XTB_CREDENTIALS` is not a valid JSON string." in str(context.exception),
                        "Expected ValueError for invalid JSON in XTB_CREDENTIALS")

    def test_xtb_credentials_not_found(self):
        """Test that a ValueError is raised if the given personal_name is not found."""
        # Set the valid credentials
        os.environ["XTB_CREDENTIALS"] = json.dumps(self.valid_credentials)

        with self.assertRaises(ValueError) as context:
            get_xtb_credentials("NonExistentUser")
        
        self.assertTrue("Credentials for 'NonExistentUser' not found." in str(context.exception),
                        "Expected ValueError for missing credentials for 'NonExistentUser'")