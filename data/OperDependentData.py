# 获取依赖case相关数据，执行依赖case获取返回结果
from util.operationExcel import OperationExcel
from data.getData import GetData
from base.runMethod import RunMethod
from jsonpath_rw import jsonpath, parse
import json

class DependentData:
    def __init__(self, caseId):
        self.caseId = caseId
        self.oper_excel = OperationExcel()
        self.get_data = GetData()


    # 根据case_id获取该行整行内容
    def get_row_data_by_caseId(self):
        row_data = self.oper_excel.get_row_value_by_caseId(self.caseId)
        return row_data

    # 执行依赖的case
    def run_dependent_case(self):
        run_method = RunMethod()
        row_Num = self.oper_excel.get_row_num_by_caseId(self.caseId)
        url = self.get_data.get_url_data(row_Num)
        method = self.get_data.get_method_data(row_Num)
        header = self.get_data.get_header_data(row_Num)
        request_data = self.get_data.get_data_for_json(row_Num)
        response_data = run_method.run_main(method, url, request_data, header)
        return json.loads(response_data)

    # 根据依赖的key，在依赖case的响应数据中找到对应的值并返回
    def get_data_by_dep_response_data(self, row):
        dep_data = self.get_data.get_dep_response_data(row)
        response_data = self.run_dependent_case()
        json_exe = parse(dep_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

#
# if __name__ == '__main__':
#     response_data = 'menu.trackNo'
#     data = {
# 	"menu": {
# 		"id": "file",
# 		"value": "OpenClose",
# 		"onclick": "OpenAndCloseDoc()",
# 		"trackNo":"201805031443vvvvvvvv",
# 		"popup": {
# 			"menuitem": [
# 				{
# 				"value": "New",
# 				"onclick": "CreateNewDoc()"
# 				},
# 				{
# 				"value": "Open",
# 				"onclick": "OpenDoc()"
# 				},
# 				{
# 				"value": "Close",
# 				"onclick": "CloseDoc()"
# 				}
# 			]
# 		}
# 		},
# "loginData":{"username":"WillyJ201804300508", "password":"Test201804300508"}
# }
#     print('-------->')
#     print(response_data)
#     print(type(response_data))
#     print(type(data))
#     print('-------->')
#     json_exe = parse(response_data)
#     madle = json_exe.find(data)
#     print([math.value for math in madle][0])
