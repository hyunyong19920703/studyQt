# Author lt_hyunyong_ki in 2024 05 14

from PySide2 import QtWidgets, QtCore, QtGui

class ItemModel():
    def __init__(self, data_dict={}):

        self.name = data_dict.get("name")
        self.age = data_dict.get("age")
        self._class = data_dict.get("class")


class CustomTableModel(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ["name", "age", "class"]

    def __init__(self, row_data=None, parent=None):
        super().__init__(parent)

        self.entri_data = []
        for _data in row_data:
            item = ItemModel(data_dict=_data)
            self.entri_data.append(item)

    def rowCount(self, parent):
        return len(self.entri_data)

    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)

    def headerData(self, row, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS
        if orientation == QtCore.Qt.Vertical:
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QAbstractTableModel.headerData(self, row, orientation, role)

    def data(self, index, role):
        row = index.row()
        column = index.column()
        item = self.entri_data[row]

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.age
            elif column == 2:
                return item._class

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled