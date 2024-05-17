# Author lt_hyunyong_ki in 2024 05 14

from importlib import reload
from PySide2 import QtWidgets, QtCore, QtGui
from ui import model_view
from model import table_model, tree_model

reload(model_view)
reload(table_model)
reload(tree_model)

table_model_source = [
    {"name": "A", "age": 10, "class": "Test"},
    {"name": "B", "age": 7, "class": "ABC"},
    {"name": "C", "age": 5, "class": "aaa"},
    {"name": "D", "age": 8, "class": "ttt"},
    {"name": "E", "age": 12, "class": "dddd"},
    {"name": "F", "age": 16, "class": "asdasd"},
    {"name": "G", "age": 13, "class": "fsdfsd"},
]

tree_model_source = [
    {"name": "A", "age": 30, "class": "Test", "children": []},
    {"name": "B", "age": 37, "class": "ABC", "children": [
        {"name": "E", "age": 12, "class": "dddd", "children": []},
        {"name": "F", "age": 16, "class": "asdasd", "children": []},
        {"name": "G", "age": 13, "class": "fsdfsd", "children": []},
    ]},
    {"name": "C", "age": 35, "class": "aaa", "children": []},
]


class ExamMain(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ExamMain, self).__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = model_view.Ui_Form()
        self.ui.setupUi(self)

        self.table_model = table_model.CustomTableModel(row_data=table_model_source)
        self.ui.tableView.setModel(self.table_model)

        # self.tree_model = tree_model.CustomTreeModel(row_data=tree_model_source)
        # self.ui.treeView.setModel(self.tree_model)


def run_execute():

    app = QtWidgets.QApplication()

    execute_main = ExamMain()
    execute_main.show()

    app.exec_()

if __name__ == "__main__":
    run_execute()
