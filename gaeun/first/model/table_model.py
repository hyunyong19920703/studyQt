# -*- coding: utf-8 -*-
__author__ = 'gaeun'

from PySide2 import *

class ItemModel():
    def __init__(self, data_dict={}):
        self.files = data_dict.get("files")
        self.type = data_dict.get("type")
        self.date = data_dict.get("date")

class CustomTableModel(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ["FILES", "FILE TYPE", "EDIT DATE"]

    def __init__(self, row_data=None, parent=None):
        super().__init__(parent)

        self.entry_data = []
        for rdata in row_data:
            item = ItemModel(data_dict=rdata)
            self.entry_data.append(item)

    def rowCount(self, parent):
        return len(self.entry_data)

    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)

    def headerData(self, row, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS[row]
        if orientation == QtCore.Qt.Vertical:
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QAbstractTableModel.headerData(self, row, orientation, role)

    def data(self, index, role):
        row = index.row()
        column = index.column()
        item = self.entry_data[row]

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return item.files
            elif column == 1:
                return item.type
            elif column == 2:
                return item.date

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
