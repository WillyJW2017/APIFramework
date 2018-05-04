import requests
import json

class RunMethod:

    def send_post(self, url, data, header = None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers = header, verify=False)
        else:
            res = requests.post(url=url,data=data, verify=False)
        # print(res.status_code)
        return res.json()

    def send_get(self, url, data = None, header = None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers = header, verify=False)
        else:
            res = requests.get(url=url,data=data, verify=False)
        return res.text

    def send_put(self, url, data = None, header = None):
        res = None
        if header != None:
            res = requests.put(url=url, data=data, headers = header, verify=False)
        else:
            res = requests.put(url=url,data=data, verify=False)
        return res.text

    def send_delete(self, url, data = None, header = None):
        res = None
        if header != None:
            res = requests.delete(url=url, data=data, headers = header, verify=False)
        else:
            res = requests.delete(url=url,data=data, verify=False)
        return res.text

    def run_main(self, method, url, data = None, header = None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data, header)
        elif method == 'PUT':
            res = self.send_put(url, data, header)
        elif method == 'DELETE':
            res = self.send_delete(url, data, header)
        elif method == 'GET':
            res = self.send_get(url, data, header)
        return json.dumps(res, sort_keys=True, indent=2, ensure_ascii=False)
