# -*- coding: utf-8 -*-
__author__ = 'gaeun'

import os, sys
from datetime import datetime

from importlib import reload
from PySide2 import *
from ui.model_test import Ui_Form
from model import table_model, tree_model

reload(table_model)
reload(tree_model)

class TestMain(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(TestMain, self).__init__(parent)
        self.setupUi(self)

        self.table_data = []
        self.data_dic = {}
        self.table_model = None
        self.data_file_path = None

        self.tablePB.clicked.connect(self.run)

    def run(self):
        self.table_data = []
        self.data_file_path = self.tablePath.text()

        file_names = os.listdir(self.data_file_path)

        for file_name in file_names:

            file_path = os.path.join(self.data_file_path, file_name)

            if os.path.isdir(file_path):
                file_type = "folder"
            else:
                file_type = os.path.splitext(file_name)[1].strip('.')

            date = os.path.getmtime(file_path)
            edit_date = datetime.fromtimestamp(date)

            self.data_dic = {
                "files": file_name,
                "type": file_type,
                "date": edit_date.strftime('%Y-%m-%d')
            }

            self.table_data.append(self.data_dic)

            self.table_model = table_model.CustomTableModel(row_data=self.table_data)
            self.tableView.setModel(self.table_model)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TestMain()
    win.show()
    sys.exit(app.exec_())