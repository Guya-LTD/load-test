import time
import random
import string
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class UserService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.1, 0.5)

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    ###
    ### Permission Endpoint
    ###
    @task
    def permissions_get(self):
        self.client.get("/api/v1/permissions")

    @task
    def permissions_post(self):
        data = {
            "name": self.get_random_string(6),
            "key": self.get_random_string(8)
        }
        self.client.post("/api/v1/permissions", json=data)

    ###
    ### Roles Endpoint
    ###
    @task
    def roles_get(self):
        self.client.get("/api/v1/roles")

    @task
    def roles_post(self):
        data = {
            "name": self.get_random_string(5),
            "uti": self.get_random_string(4)
        }
        self.client.post("/api/v1/roles")

    @task
    def roles_get_by_id(self):
        self.client.get("/api/v1/roles/1")

    
    