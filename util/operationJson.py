# 操作json格式数据的封装
import json

class OperationJson:
    def __init__(self, filePath = None):
        if filePath:
            self.filePath = filePath
        else:
            self.filePath = 'C:\\Willy\\Study\\API\\test.json'
        self.returnData = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.filePath) as fp:
            data = json.load(fp)
            return data

    # 写json文件
    def write_data(self, data):
        with open(self.filePath, 'w') as fp:
            fp.write(json.dumps(data))

    # 根据关键字获取数据
    def get_data(self, key):
        return  self.returnData[key]

    # 获取cookie

#
# if __name__ == '__main__':
#     op = OperationJson()
#     print(op.get_data('loginData'))
