import time
import json
from locust import HttpUser, task, between

class Branch(HttpUser):
    wait_time = between(1, 2)

    @task
    def get(self):
        headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
        }
        self.client.get('/branches')

    @task
    def post(self):
        headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
        }
        self.client.post(
            '/branches',
            headers = headers,
            json = {
                "manager_id": "88",
                "names": {"en": "Abc", "am": "aa"},
                "location": {
                    "woreda": "07",
                    "kebele": "03",
                    "house_no": "444",
                    "gps": [-11, -33]
                }
            }
        )