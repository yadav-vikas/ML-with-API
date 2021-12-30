from django.http import response
from django.test import TestCase
from rest_framework.test import APIClient # Testcase didnt pass on this one
from django.test import Client

# Client and APIClient are similar 1 is from django and other is from Rest-framework
# APICLIENT is having import error 


class EndpointTests(TestCase):

    def test_predict_view(self):
        client = Client()
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        classifier_url = "/api/v1/income_classifier/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["label"], "<=50k")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
