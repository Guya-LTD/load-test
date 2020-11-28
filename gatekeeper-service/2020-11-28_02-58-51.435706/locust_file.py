import time
from locust import HttpUser, task

class GatekeeperService(HttpUser):
    @task
    def sessions_post(self):
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        self.client.post("/api/v1/sessions", json=data)