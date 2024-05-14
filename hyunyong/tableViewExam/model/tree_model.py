# Author lt_hyunyong_ki in 2024 05 14

from PySide2 import QtWidgets, QtCore, QtGui
HORIZONTAL_HEADERS = ["name", "age", "class"]

class ItemModel():

    def __init__(self, data={}, parentItem=None):

        self.name = data.get("name")
        self.age = data.get("age")
        self._class = data.get("class")

        self.parentItem = parentItem
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self) -> int:
        return len(HORIZONTAL_HEADERS)

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0



class CustomTreeModel(QtCore.QAbstractItemModel):

    def __init__(self, row_data=None, parent=None):
        super().__init__(parent)

        self.entri_data = row_data
        self.rootItem = ItemModel()

        self.parents = {0: self.rootItem}

        for _data in self.entri_data:

            self.init_data(_data=_data, parent=self.rootItem)

    def init_data(self, _data=dict(), parent=ItemModel()):

        new_item = ItemModel(data=_data, parentItem=parent)
        parent.appendChild(new_item)

        if _data.get("children"):
            for child in _data.get("children"):
                self.init_data(_data=child, parent=new_item)

    def data(self, index=QtCore.QModelIndex(), role=QtCore.Qt.DisplayRole):

        row = index.row()
        column = index.column()
        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.age
            elif column == 2:
                return item._class


    def rowCount(self, parent=QtCore.QModelIndex()):

        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parent_item = self.rootItem
        else:
            parent_item = parent.internalPointer()

        return parent_item.childCount()

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(HORIZONTAL_HEADERS)

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.childItems[row]

        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index=QtCore.QModelIndex()):

        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()

        if not childItem:
            return QtCore.QModelIndex()

        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def headerData(self, column, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            try:
                return HORIZONTAL_HEADERS[column]
            except IndexError:
                pass
        return None

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        start, end = position, rows
        self.beginRemoveRows(parent, start, end)
        del self._data[start:end + 1]
        self.endRemoveRows()
        return True

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
