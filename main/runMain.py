from base.runMethod import RunMethod
from data.getData import GetData
from data.OperDependentData import DependentData
from util.CommonUtil import CommonUtil

class RunMain:
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.common_util = CommonUtil()

    def run_test_flow(self):
        res = None
        pass_count = []
        fail_count = []
        rowNum = self.get_data.get_case_numbers()
        for i in range(2, rowNum + 1):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                url = self.get_data.get_url_data(i)
                method = self.get_data.get_method_data(i)
                header = self.get_data.get_header_data(i)
                request_data = self.get_data.get_data_for_json(i)
                expect_data = self.get_data.get_expect_data(i)
                dep_caseId = self.get_data.get_dep_caseId(i)
                # 如果有依赖的case要执行，则执行依赖case并获取依赖case的返回数据
                if dep_caseId != None:
                    self.dep_data = DependentData(dep_caseId)
                    dep_response_data = self.dep_data.get_data_by_dep_response_data(i)
                    dep_field_data = self.get_data.get_dep_field_data(i)
                    request_data[dep_field_data] = dep_response_data

                # method, url, data = None, header = None
                res = self.run_method.run_main(method, url, request_data, header)
                compareResult = self.common_util.is_contain(expect_data, res)
                if compareResult:
                    print('This test case passed')
                    self.get_data.write_result(i, 'Passed')
                    pass_count.append(i)
                else:
                    print('This test case failed')
                    self.get_data.write_result(i, res)
                    fail_count.append(i)
                print(res)
                # return res
        print(len(pass_count))
        print(len(fail_count))






if __name__ == '__main__':
    runmain = RunMain()
    runmain.run_test_flow()
