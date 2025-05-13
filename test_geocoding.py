import unittest
from graphhopper_parse_json import geocoding



class TestGeocoding(unittest.TestCase):
    def test_valid_location(self):
        status, lat, lng, loc = geocoding("Cebu", "d25591a8-cbbc-456d-8e3d-8a5f63420189")
        self.assertEqual(status, 200)
        self.assertNotEqual(lat, "null")
        self.assertNotEqual(lng, "null")

    def test_invalid_location(self):
        status, lat, lng, loc = geocoding("asdkjasd@!@#", "d25591a8-cbbc-456d-8e3d-8a5f63420189")
        self.assertTrue(status != 200 or lat == "null" or lng == "null")

if __name__ == '__main__':
    unittest.main()
