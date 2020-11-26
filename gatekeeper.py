import time
import gevent
from locust import HttpUser, task
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging

setup_logging("INFO", None)

class GatekeeperUser(HttpUser):
    DNS = "http://127.0.0.1:60007"

    @task
    def sessions(self):
        URL = DNS + "/api/v1/sessions"
        data = {
            "identity": "admin0@localhost.com",
            "password": "admin"
        }
        self.client.post(URL)

## Setup Environment and Runner
env = Environment(user_classes = [GatekeeperUser])
env.create_local_runner()

## Start a WebUI instance
env.create_web_ui("127.0.0.1", 8080)

## Start a greenlet the periodically outpus the current stats
gevent.spawn(stats_printer(env.stats))

## Start a greenlet that save current stats to history
gevent.spawn(stats_history, env.runner)

## Start the test
env.runner.start(1, spawn_rate = 10)

## In 60 seconds stop the runner
gevent.spawn_later(60, lambda: env.runner.quit())

## Wait for the greenlets
env.runner.greenlet.join()

## Stop the web server for good measures
env.web_ui.stop()