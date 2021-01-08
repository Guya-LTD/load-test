import time
import random
import string
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class BranchService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.1, 0.5)

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    ###
    ### Branches Endpoint
    ###
    @task
    def branches_get(self):
        self.client.get("/api/v1/branches")

    @task
    def permissions_post(self):
        """Login"""
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        response = self.client.post("http://127.0.0.1:60007/api/v1/sessions", json=data)
        token = json.loads(response._content)['data']['token']
        ## Set Authorization Headers
        headers = {"Authorization": "Bearer " + token}

        data = {
            "name": {
                "en": self.get_random_string(6),
                "am": self.get_random_string(8)
            },
            "location": {
                "woreda": self.get_random_string(2),
                "kebele": self.get_random_string(2),
                "house_no": self.get_random_string(4),
                "gps": [-15, -13]
            },
            "manager_id": self.get_random_string(3),
            "company": "shop"
        }
        self.client.post("/api/v1/branches", headers=headers, json=data)

    @task
    def permission_get(self):
        id = 33
        self.client.get("/api/v1/branches/" + id)

    @task
    def permission_delete(self):
        id = 44
        self.client.delete("/api/v1/branches/" + id)

    
    