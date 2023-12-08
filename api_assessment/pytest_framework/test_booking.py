import requests
import json
import pytest
import logging

import base64


username = 'admin'
password = 'password123'


credentials = f"{username}:{password}"


encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')


print(encoded_credentials)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RestfulBookerAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_credentials}",
        }

    def create_booking(self, data):
        url = f"{self.base_url}/booking"
        response = requests.post(url, json=data, headers=self.headers)
        logger.info(f"Create Booking - Status Code: {response.status_code}, Response: {response.text}")
        return response

    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.get(url, headers=self.headers)
        logger.info(f"Get Booking - Status Code: {response.status_code}, Response: {response.text}")
        return response

    def update_booking(self, booking_id, data):
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.put(url, json=data, headers=self.headers)
        logger.info(f"Update Booking - Status Code: {response.status_code}, Response: {response.text}")
        print(response.text)
        return response

    def delete_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.delete(url, headers=self.headers)
        logger.info(f"Delete Booking - Status Code: {response.status_code}, Response: {response.text}")
        return response

@pytest.fixture
def api_client():
    base_url = "https://restful-booker.herokuapp.com"
    return RestfulBookerAPIClient(base_url)

def test_create_booking(api_client):
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-05"},
    }

    response = api_client.create_booking(data)
    assert response.status_code == 200
    logger.info("Create Booking Test Passed")


def test_get_booking(api_client):

    booking_id = 1
    response = api_client.get_booking(booking_id)
    assert response.status_code == 200
    logger.info("Get Booking Test Passed")


def test_update_booking(api_client):

    booking_id = 1
    data = {"firstname": "rahul", "lastname": "dravid"}

    response = api_client.update_booking(booking_id, data)
    assert response.status_code == 200
    logger.info("Update Booking Test Passed")

def test_delete_booking(api_client):
    booking_id = 1
    response = api_client.delete_booking(booking_id)
    assert response.status_code == 201


    response = api_client.get_booking(booking_id)
    assert response.status_code == 404
    logger.info("Delete Booking Test Passed")
