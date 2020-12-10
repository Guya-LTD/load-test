import time
import random
import string
import json
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class PaymentServie(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.1, 0.5)

    def on_start(self):
        """Login"""
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        response = self.client.post("http://127.0.0.1:60007/api/v1/sessions", json=data)
        token = json.loads(response._content)['data']['token']
        ## Set Authorization Headers
        self.headers = {"Authorization": "Bearer " + token}
        ## Get ids
        self.RESS_PAYMENTS = []
        self.RESS_TRANSACTION = []

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    ###
    ### Payments Endpoint
    ###
    @task(1)
    def payments_get(self):
        res = self.client.get("/api/v1/payments")
        self.RESS_PAYMENTS = res.json()['data']

    @task
    def payments_post(self):
        data = {
            "invoice_number": self.get_random_string(3),
            "transaction_id": self.get_random_string(6),
            "transaction_date": "10/02/2020",
            "transaction_medium": "MBirr"
        }
        self.client.post("/api/v1/payments", headers=self.headers, json=data)

    @task
    def payment_get(self):
        if self.RESS_PAYMENTS:
            id = (random.choice(self.RESS_PAYMENTS))['_id']['$oid']
        else:
            id = self.get_random_string(12)
        self.client.get("/api/v1/payments/" + id)

    @task
    def payment_put(self):
        if self.RESS_PAYMENTS:
            id = (random.choice(self.RESS_PAYMENTS))['_id']['$oid']
        else:
            id = self.get_random_string(12)
        data = {
            "invoice_number": self.get_random_string(3),
            "transaction_id": self.get_random_string(6),
            "transaction_date": "10/02/2020",
            "transaction_medium": "MBirr"
        }
        self.client.put("/api/v1/payments/" + id, headers=self.headers, json=data)

    ###
    ### Transaction Endpoint
    ###
    @task(1)
    def transactions_get(self):
        res = self.client.get("/api/v1/transactions")
        self.RESS_TRANSACTION = res.json()['data']

    @task
    def transactions_post(self):
        data = {
            "transaction_id": self.get_random_string(6),
            "transaction_date": "10/02/2020",
            "transaction_medium": "MBirr",
            "amount": str(random.randint(100, 1000)),
            "flag": ""
        }
        self.client.post("/api/v1/transactions", headers=self.headers, json=data)

    @task
    def transaction_get(self):
        if self.RESS_TRANSACTION:
            id = (random.choice(self.RESS_TRANSACTION))['_id']['$oid']
        else:
            id = self.get_random_string(12)
        self.client.get("/api/v1/transactions/" + id)

    @task
    def transaction_put(self):
        if self.RESS_TRANSACTION:
            id = (random.choice(self.RESS_TRANSACTION))['_id']['$oid']
        else:
            id = self.get_random_string(12)
        data = {
            "transaction_id": self.get_random_string(6),
            "transaction_date": "10/02/2020",
            "transaction_medium": "MBirr",
            "amount": str(random.randint(100, 1000)),
            "flag": ""
        }
        self.client.put("/api/v1/transactions/" + id, headers=self.headers, json=data)