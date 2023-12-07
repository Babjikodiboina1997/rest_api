import unittest
import requests

class TestRestfulBookerAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.booking_id = None

    def test_create_booking(self):
        booking_data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 500,
            "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-05"},
            "additionalneeds": "Breakfast"
        }

        response = requests.post(f"{self.base_url}/booking", json=booking_data)
        self.assertEqual(response.status_code, 200)
        self.booking_id = response.json().get("bookingid")

    def test_get_booking(self):
        self.assertIsNotNone(self.booking_id, "Booking ID is required for this test.")
        response = requests.get(f"{self.base_url}/booking/{self.booking_id}")
        self.assertEqual(response.status_code, 200)

    def test_update_booking(self):
        self.assertIsNotNone(self.booking_id, "Booking ID is required for this test.")
        update_data = {"firstname": "UpdatedName"}
        response = requests.put(f"{self.base_url}/booking/{self.booking_id}", json=update_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_booking(self):
        # Ensure the booking_id is set before attempting to delete
        self.assertIsNotNone(self.booking_id, "Booking ID is required for this test.")
        response = requests.delete(f"{self.base_url}/booking/{self.booking_id}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
