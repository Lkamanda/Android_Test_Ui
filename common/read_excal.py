# @Time       :      2020/3/22 10:23
# @Description:  读取 excal

import xlrd
import os
from common.custom import gsb

class ReadExcal(object):

    def __init__(self):
        excalP= "{0}{1}testData{1}".format(os.path.dirname(os.path.dirname(__file__)), gsb())
        excal_path = os.path.join(excalP, 'test.xls')
        readbook = xlrd.open_workbook(excal_path)
        self.first_sheet = readbook.sheet_by_index(0)
        self.data_list = []


    def get_content(self, className, methodName, x):
        #  className, methodName
        # 根据类名和方法名获取测试数据

        # 最大行数
        nrows = self.first_sheet.nrows
        for i in range(1, nrows):
            # 获取第n列的数据
            row_value = self.first_sheet.row_values(i)
            if row_value[1] == className and row_value[2] == methodName:
                self.data_list.append(row_value[-1])
        print(self.data_list)
        return self.data_list[x]

if __name__ == '__main__':
    rd = ReadExcal()
    print(rd.get_content('Test_Home', 'test_search',1))
