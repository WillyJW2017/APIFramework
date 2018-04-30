# 操作json格式数据的封装
import json

class OperationJson:
    def __init__(self, filePath = None):
        if filePath:
            self.filePath = filePath
        else:
            self.filePath = 'C:\\Willy\\Study\\API\\test.json'
        self.returnData = self.read_data()

    def read_data(self):
        with open(self.filePath) as fp:
            data = json.load(fp)
            return data

    def get_data(self, key):
        return  self.returnData[key]

if __name__ == '__main__':
    op = OperationJson()
    print(op.get_data('login'))
