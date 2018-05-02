from base.runMethod import RunMethod
from data.getData import GetData
from util.CommonUtil import CommonUtil

class RunMain:
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.common_util = CommonUtil()

    def run_test_flow(self):
        res = None
        rowNum = self.get_data.get_case_numbers()
        for i in range(2, rowNum + 1):
            url = self.get_data.get_url_data(i)
            method = self.get_data.get_method_data(i)
            header = self.get_data.get_header_data(i)
            request_data = self.get_data.get_data_for_json(i)
            expect_data = self.get_data.get_expect_data(i)
            run = self.get_data.get_is_run(i)
            if run:
                # method, url, data = None, header = None
                res = self.run_method.run_main(method, url, request_data, header)
                compareResult = self.common_util.is_contain(expect_data, res)
                if compareResult:
                    print('This test case pass')
                else:
                    print('This test case failed')
            print(res)
            # return res

if __name__ == '__main__':
    runmain = RunMain()
    runmain.run_test_flow()
