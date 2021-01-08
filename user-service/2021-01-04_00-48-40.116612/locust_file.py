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
            "uti": self.get_random_string(4),
            'permissions': []
        }
        self.client.post("/api/v1/roles", json=data)

    @task
    def roles_get_by_id(self):
        self.client.get("/api/v1/roles/1")

    ###
    ### Users Endpoint
    ###
    @task
    def users_get(self):
        self.client.get('/api/v1/users')

    @task
    def users_post(self):
        pnum = ''
        for x in range(13):
            pnum += random.randint(0, 9)
        data = {
            "name": self.get_random_string(6),
            "identity": self.get_random_string(6),
            "password": self.get_random_string(10),
            "uti": 'CU_3310',
            'email': self.get_random_string(5) + '@testing.com',
            'pnum': pnum
        }
        self.client.post('/api/v1/users', json=data)
    
    @task
    def users_delete(self):
        self.client('/api/v1/users/' + random.randint(1, 100))

    ###
    ### Credentials Endpoint
    ###
    @task
    def credentials_post(self):
        data = {
            'identity': self.get_random_string(10),
            'password': self.get_random_string(10)
        }
        self.client('/api/v1/credentials', json=data)