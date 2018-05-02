# 获取每个case的所有数据
from util.operationExcel import OperationExcel
from util.operationJson import OperationJson
import data.dataConfig

class GetData:
    def __init__(self):
        self.oper_excel = OperationExcel()
        self.oper_json = OperationJson()

    def get_case_numbers(self):
        return self.oper_excel.get_rows()

    # 获取excel里面URL列的数据
    def get_url_data(self, row):
        col = int(data.dataConfig.get_url())
        url_data = self.oper_excel.get_cell_data(row, col)
        return url_data

    # 获取excel里面Method列的数据
    def get_method_data(self, row):
        col = int(data.dataConfig.get_method())
        method_data = self.oper_excel.get_cell_data(row, col)
        return method_data

    # 获取excel里面Header列的数据
    def get_header_data(self, row):
        col = int(data.dataConfig.get_header())
        head_data = self.oper_excel.get_cell_data(row, col)
        if head_data == 'YES':
            return data.dataConfig.get_header_value()
        else:
            return None

    # 获取excel里面RequestData列的数据
    def get_request_data(self, row):
        col = int(data.dataConfig.get_request_data())
        request_data = self.oper_excel.get_cell_data(row, col)
        if request_data == '':
            return None
        print(request_data)
        return request_data


    # 通过指定key从json文件里面获取数据
    def get_data_for_json(self, row):
        req_value = self.oper_json.get_data(self.get_request_data(row))
        return req_value

    # 获取excel里面ExpectedData列的数据
    def get_expect_data(self, row):
        col = int(data.dataConfig.get_expect_data())
        expect_data = self.oper_excel.get_cell_data(row, col)
        if expect_data == '':
            return None
        return expect_data

    # 获取excel里面Run列的数据
    def get_is_run(self, row):
        flag = None
        col = int(data.dataConfig.get_run())
        run_data = self.oper_excel.get_cell_data(row, col)
        if run_data == 'YES':
            flag = True
        else:
            flag = False
        return flag

    def write_result(self, row, value):
        col = int(data.dataConfig.get_actual_result())
        self.oper_excel.write_data(row, col, value)
