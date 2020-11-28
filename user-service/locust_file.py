import time
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class UserService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.5, 10)

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @task
    def permissions_get(self):
        self.client.get("/api/v1/permissions")

    @task
    def permissions_post(self):
        data = {
            "name": get_random_string(6),
            "key": get_random_string(8)
        }