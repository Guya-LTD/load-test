import time
import json
import random
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class GatekeeperService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.1, 0.5)

    def on_start(self):
        """Login"""
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        response = self.client.post("/api/v1/sessions", json=data)
        token = json.loads(response._content)['data']['token']
        ## Set Authorization Headers
        self.headers = {"Authorization": "Bearer" + token}

    ##
    ## Carts endpoint
    ##
    @task
    def carts_get(self):
        self.client.get(
            "/api/v1/carts",
            headers = self.headers
        )

    ##
    ## Carts Items endpoint
    ##
    @task
    def carts_items_post(self):
        data = {
            "product_id": random.randint(1, 1000),
            "quantity": random.randint(1, 10)
        }
        self.client.post("/api/v1/carts/items", headers=self.headers, json=data)

    @task
    def carts_items_delete(self):
        self.client.delete("/api/v1/carts/items/" + random.randint(1, 100), headers=self.headers)