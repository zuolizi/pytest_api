import os.path

import openpyxl
from utils.handle_path import *


class Handle_Excel():

    def __init__(self, filename, sheet_name=None):
        self.filename = filename
        self.lwb = openpyxl.load_workbook(filename=self.filename)
        if sheet_name is not None:
            self.set_sheet(sheet_name)

    def set_sheet(self, sheet_name):
        self.sh = self.lwb[sheet_name]
        self.rows = list(self.sh.rows)
        self.th = [i.value for i in self.rows[0]]

    def first_line(self):
        return dict(zip(self.th, [j.value for j in self.rows[1]]))

    def read_data(self):
        return [dict(zip(self.th, [j.value for j in i])) for i in self.rows[1:]]

    def write_data(self, row, column, value):
        self.sh.cell(row=row, column=column, value=value)
        self.lwb.save(self.filename)


if __name__ == '__main__':
    filename = os.path.join(data_path, 'data.xlsx')
    sheet_name = 'login'
    he = Handle_Excel(filename)
    he.set_sheet(sheet_name)
    print(he.first_line())
    he.write_data(2, 8, '通过')
    print(he.read_data())
