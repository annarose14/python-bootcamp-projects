import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

# Configure logging
logging.basicConfig(level=logging.INFO)

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = None
        self._token_expiry = None
        self.get_new_token_if_expired()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        if response.status_code != 200:
            logging.error("Failed to obtain token: %s", response.text)
            return None

        token_info = response.json()
        self._token = token_info['access_token']
        self._token_expiry = datetime.now() + timedelta(seconds=token_info['expires_in'])
        logging.info("New token obtained: %s", self._token)
        logging.info("Token expires in %d seconds", token_info['expires_in'])

    def _is_token_expired(self):
        return self._token_expiry is None or datetime.now() >= self._token_expiry

    def get_new_token_if_expired(self):
        if self._is_token_expired():
            self._get_new_token()

    def get_destination_code(self, city_name):
        self.get_new_token_if_expired()
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            logging.error("Failed to fetch destination code: %s", response.text)
            return "Not Found"

        logging.info("Response data for city search: %s", response.json())
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            logging.warning("No airport code found for %s.", city_name)
            return "N/A"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        if from_time < datetime.now() or to_time < datetime.now():
            logging.warning("Departure and return dates must be in the future.")
            return None

        self.get_new_token_if_expired()
        logging.info("Using token: %s", self._token)  # Debugging the token
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            logging.error("check_flights() response code: %s", response.status_code)
            logging.error("There was a problem with the flight search: %s", response.text)
            return None

        return response.json()
