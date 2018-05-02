# 操作Excel数据类的封装

import openpyxl

class OperationExcel:
    def __init__(self, filePath=None, sheetName=None):
        defaultfilePath = 'C:\\Willy\\Study\\API\\TestCase.xlsx'
        if filePath:
            self.filePath = filePath
            self.sheetName = sheetName
        else:
            self.filePath = defaultfilePath
            self.sheetName = 'TestCases'
        self.load_excel()

    # 加载excel，激活指定sheet
    def load_excel(self):
        self.workbook = openpyxl.load_workbook(self.filePath)
        self.sheet = self.workbook[self.sheetName]

    # 获取指定单元格内容
    def get_cell_data(self, rowNum, colNum):
        cell_data = self.sheet.cell(row=rowNum, column=colNum).value
        return cell_data

    # 获取行数
    def get_rows(self):
        row = self.sheet.max_row
        return row

    # 获取列数
    def get_cols(self):
        col = self.sheet.max_column
        return col

    # 写入数据到excel
    def write_data(self, row, col, value):
        self.sheet.cell(row=row, column=col, value=value)
        self.workbook.save(filename = self.filePath)

    def get_row_value(self, row):

        rowValue = self.sheet.iter_rows(min_col=1, min_row=1, max_col=self.sheet.max_column, max_row=self.sheet.max_row)

        return rowValue

if __name__ == '__main__':
#     # op = operationExcel('C:\\Willy\\Study\\API\\test.xlsx', 'UFTConfig')
    op = OperationExcel()
#     # print(op.get_cell_data(4, 1))
#     # print(op.get_lines())
#     op.write_data(10,1,'PASS!!!')
    print(op.get_row_value(2))
