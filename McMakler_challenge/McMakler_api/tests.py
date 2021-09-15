import json
from rest_framework.test import APITestCase

'''Test a sample respose'''
class ResponseTestCase(APITestCase):
    def test_get_result(self):
        response = self.client.get('/get-stats/?field=mssubclass&method=common')
        self.assertEqual(json.loads(response.content), [{'result': 20}])
