import time
from locust import HttpUser, task, between

#import resource
#resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class GatekeeperService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.5, 10)

    @task
    def sessions_post(self):
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        self.client.post("/api/v1/sessions", json=data)
