import os
import requests
import unittest

os.environ['NO_PROXY'] = '127.0.0.1'
endpoint = "http://127.0.0.1:5000"


class TestHotels(unittest.TestCase):
    def test_hotels(self):
        result = requests.get(f'{endpoint}/hotels').json()
        self.assertEqual(len(result), 5, "Should return 5 hotels")
        for hotel in result:
            self.assertIn("name", hotel, "Hotels should have a name field")
            self.assertIn("stars", hotel, "Hotels should have a stars field")
            self.assertIn("destination", hotel,
                          "Hotels should have a destination field")

        test_hotel = {'name': 'Hotel Mountain Budget',
                      'stars': 2, 'destination': 'Tyrol'}
        self.assertIn(test_hotel, result,
                      "All hotels should contain one of the hotels")

    def test_1_star(self):
        result = requests.get(f'{endpoint}/hotels?stars=1').json()
        expected_result = []
        self.assertEqual(result, expected_result,
                         "Should return empty list for 1 star hotels")

    def test_3_star(self):
        result = requests.get(f'{endpoint}/hotels?stars=3').json()
        hotel_playa = {"name": "Hotel Playa",
                       "stars": 3, "destination": "Mallorca"}
        self.assertIn(hotel_playa, result,
                      "3 star hotels should contain hotel playa")
        for hotel in result:
            self.assertEqual(hotel["stars"], 3, "Hotel should be 3 star")

    def test_7_star(self):
        result = requests.get(f'{endpoint}/hotels?stars=7')
        expected_result = "Stars should be between 1 and 5"
        self.assertEqual(result.text, expected_result,
                         "Should warn when stars is out of range")

    def test_invalid_stars(self):
        result = requests.get(f'{endpoint}/hotels?stars=someText')
        expected_result = "Stars should be valid integer"
        self.assertEqual(result.text, expected_result,
                         "Should warn when stars is not valid")


if __name__ == '__main__':
    unittest.main()
