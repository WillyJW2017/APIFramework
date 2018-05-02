import requests
import json

class RunMethod:

    def send_post(self, url, data, header = None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers = header)
        else:
            res = requests.post(url=url,data=data)
        print(res.status_code)
        return res.json()

    def send_get(self, url, data = None, header = None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers = header)
        else:
            res = requests.get(url=url,data=data)
        return res.text

    def run_main(self, method, url, data = None, header = None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data, header)
        else:
            res = self.send_get(url, data, header)
        return json.dumps(res, sort_keys=True, indent=2, ensure_ascii=False)
