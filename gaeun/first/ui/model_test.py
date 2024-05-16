# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model_test.ui'
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
        Form.resize(800, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 19, 761, 861))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableSide = QVBoxLayout()
        self.tableSide.setSpacing(10)
        self.tableSide.setObjectName(u"tableSide")
        self.tableSide.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableLabel = QLabel(self.horizontalLayoutWidget)
        self.tableLabel.setObjectName(u"tableLabel")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.tableLabel.setFont(font)
        self.tableLabel.setLayoutDirection(Qt.LeftToRight)
        self.tableLabel.setTextFormat(Qt.PlainText)
        self.tableLabel.setScaledContents(False)
        self.tableLabel.setAlignment(Qt.AlignCenter)

        self.tableSide.addWidget(self.tableLabel)

        self.tablePath = QLineEdit(self.horizontalLayoutWidget)
        self.tablePath.setObjectName(u"tablePath")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(8)
        self.tablePath.setFont(font1)
        self.tablePath.setClearButtonEnabled(True)

        self.tableSide.addWidget(self.tablePath)

        self.tablePB = QPushButton(self.horizontalLayoutWidget)
        self.tablePB.setObjectName(u"tablePB")

        self.tableSide.addWidget(self.tablePB)

        self.tableView = QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableView.setAutoScrollMargin(15)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(40)
        self.tableView.horizontalHeader().setDefaultSectionSize(120)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setMinimumSectionSize(30)
        self.tableView.verticalHeader().setDefaultSectionSize(35)

        self.tableSide.addWidget(self.tableView)


        self.horizontalLayout.addLayout(self.tableSide)

        self.treeSide = QVBoxLayout()
        self.treeSide.setSpacing(10)
        self.treeSide.setObjectName(u"treeSide")
        self.treeSide.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.treeSide.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.treeSide.addWidget(self.lineEdit_2)

        self.treeView = QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName(u"treeView")

        self.treeSide.addWidget(self.treeView)


        self.horizontalLayout.addLayout(self.treeSide)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tableLabel.setText(QCoreApplication.translate("Form", u"Table View", None))
        self.tablePath.setText(QCoreApplication.translate("Form", u"\uacbd\ub85c\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.tablePB.setText(QCoreApplication.translate("Form", u"GET", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tree View", None))
    # retranslateUi

