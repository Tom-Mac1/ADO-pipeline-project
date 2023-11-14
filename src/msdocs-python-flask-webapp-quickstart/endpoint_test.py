import unittest
import requests

class TestEndpoint(unittest.TestCase):
    def test_hello_endpoint(self):
        url = "http://localhost:5000/hello?name=Tom"

        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertIn("hello", response.text.lower())

if __name__ == '__main__':
    unittest.main()
