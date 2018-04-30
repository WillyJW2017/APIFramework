import requests
import json

class RunMain:
    # def __init__(self, url, method, data = None):
    #     self.res = self.run_main(url, method, data)

    def send_post(self, url, datadict):
        res = requests.post(url=url,data=datadict).json()
        return json.dumps(res)

    def send_get(self, url, datadict):
        res = requests.get(url=url,data=datadict).json()
        return json.dumps(res)

    def run_main(self, url, method, data = None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        return res


# if __name__ == '__main__':
#     datadict = {
#         'username': 'HelloWorld',
#         'password': 'Welcome'
#     }
#     url = 'http://127.0.0.1:8000/login/'
#
#     run = RunMain(url, 'POST', datadict)
#     print(run.res)