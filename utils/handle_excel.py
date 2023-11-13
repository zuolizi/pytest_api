import os.path

import openpyxl
from utils.handle_path import *


class Handle_Excel():

    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.lwb = openpyxl.load_workbook(filename=self.filename)
        self.sh = self.lwb[sheet_name]
        # <generator object Worksheet._cells_by_row at 0x0000014093A28C10>

    def get_sheet_rows(self,sheet_name):
        return self.lwb[sheet_name].rows

    def first_line(self):
        rows = list(self.sh.rows)
        return dict(zip([i.value for i in rows[0]], [j.value for j in rows[1]]))

    def read_data(self):
        rows = list(self.sh.rows)
        return [dict(zip([i.value for i in rows[0]], [j.value for j in i])) for i in rows[1:]]

    def write_data(self, row, column, value):
        self.sh.cell(row=row, column=column, value=value)
        self.lwb.save(self.filename)


if __name__ == '__main__':
    filename = os.path.join(data_path, 'data.xlsx')
    sheet_name = 'login'
    he = Handle_Excel(filename, sheet_name)
    he.get_sheet_rows(sheet_name)
    # he.write_data(2, 8, '通过')
    # print(he.read_data())

