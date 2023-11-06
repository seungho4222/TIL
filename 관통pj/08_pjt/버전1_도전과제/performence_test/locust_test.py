from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    # @task
    # def data(self):
    #     self.client.get("test/data/")

    # @task
    # def nan_data(self):
    #     self.client.get("test/nan_data/")

    @task
    def algorithm(self):
        self.client.get("test/algorithm/")


