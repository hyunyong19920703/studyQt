# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(849, 690)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.tableBtn = QPushButton(Form)
        self.tableBtn.setObjectName(u"tableBtn")

        self.verticalLayout_2.addWidget(self.tableBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.treeView = QTreeView(Form)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)

        self.treeBtn = QPushButton(Form)
        self.treeBtn.setObjectName(u"treeBtn")

        self.verticalLayout.addWidget(self.treeBtn)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Table View", None))
        self.tableBtn.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tree View", None))
        self.treeBtn.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

