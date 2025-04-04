from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def index_page(self):
        self.client.get("/")

    @task
    def about_page(self):
        self.client.get("/about")  # Referință la /about

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)