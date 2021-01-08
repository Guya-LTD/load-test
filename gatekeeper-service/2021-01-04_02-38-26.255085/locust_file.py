import time
from locust import HttpUser, task, between

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

class GatekeeperService(HttpUser):
    ## Random wait time between 0.5 and 10 seconds 
    wait_time = between(0.1, 0.5)

    @task
    def sessions_post(self):
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        self.client.post("/api/v1/sessions", json=data)

    @task
    def session_get(self):
        headers = {"Authorization": "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImNyZWF0ZWRfYXQiOiIyMDIwLTEyLTAxVDAxOjI0OjA5LjY5NTUyMSIsImNyZWRlbnRpYWwiOnsiYmxvY2tlZCI6ZmFsc2UsImlkIjo3LCJpZGVudGl0eSI6ImFkbWluMEBsb2NhbGhvc3QuY29tIiwibm90ZSI6bnVsbCwidXBkYXRlZF9hdCI6IjIwMjAtMTItMDFUMDE6MjQ6MDkuNjk4MTM2In0sImVtYWlsIjoiYWRtaW4wQGxvY2FsaG9zdC5jb20iLCJpZCI6MjgsIm5hbWUiOiJcdTEyNjBcdTEyMDhcdTEzMjEgXHUxMjYzXHUxMjA1XHUxMjI5IiwicG51bSI6bnVsbCwicm9sZSI6eyJjcmVhdGVkX2F0IjoiMjAyMC0xMi0wMVQwMToyMzowNy45MTcyMTYiLCJjcmVhdGVkX2J5IjoxLCJpZCI6MTE2LCJuYW1lIjoiRS1jb21tZXJjZSAtIEFkbWluIiwicGVybWlzc2lvbnMiOltdLCJ1cGRhdGVkX2F0IjoiMjAyMC0xMi0wMVQwMToyMzowNy45MTcyMjAiLCJ1cGRhdGVkX2J5IjpudWxsLCJ1dGkiOiJBRF8yMTEwIn0sInJvbGVfaWQiOjExNiwidXBkYXRlZF9hdCI6IjIwMjAtMTItMDFUMDE6MjQ6MDkuNjk1NTI1In0sIm1lc3NhZ2UiOiJDcmVkZW50aWFsIG1hdGNoZWQiLCJzdGF0dXMiOiJPSyIsInN0YXR1c19jb2RlIjoyMDB9.pCfN7SoRVuxRv8TkeWi_ttzX4iE2BXMjj4wcX_QZ1l8"}
        self.client.post('/api/v1/sessions/0',  headers=headers)