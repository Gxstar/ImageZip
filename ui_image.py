# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 500)
        Form.setMinimumSize(QSize(640, 500))
        Form.setMaximumSize(QSize(640, 500))
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.imageList = QListWidget(Form)
        self.imageList.setObjectName(u"imageList")

        self.horizontalLayout_5.addWidget(self.imageList)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(158, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.theight = QLineEdit(self.groupBox)
        self.theight.setObjectName(u"theight")
        self.theight.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout_2.addWidget(self.theight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.twidth = QLineEdit(self.groupBox)
        self.twidth.setObjectName(u"twidth")
        self.twidth.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout_3.addWidget(self.twidth)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.tsize = QLineEdit(self.groupBox)
        self.tsize.setObjectName(u"tsize")
        self.tsize.setMinimumSize(QSize(60, 0))
        self.tsize.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout_4.addWidget(self.tsize)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.tdpi = QLineEdit(self.groupBox)
        self.tdpi.setObjectName(u"tdpi")
        self.tdpi.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.tdpi)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.bar = QProgressBar(Form)
        self.bar.setObjectName(u"bar")
        self.bar.setValue(0)

        self.verticalLayout_2.addWidget(self.bar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.importButton = QPushButton(Form)
        self.importButton.setObjectName(u"importButton")

        self.horizontalLayout.addWidget(self.importButton)

        self.zipButton = QPushButton(Form)
        self.zipButton.setObjectName(u"zipButton")

        self.horizontalLayout.addWidget(self.zipButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u76ee\u6807\u5927\u5c0f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9ad8\uff1a", None))
        self.theight.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bbd\uff1a", None))
        self.twidth.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u5927\u5c0f\uff08KB\uff09\uff1a", None))
        self.tsize.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76ee\u6807dpi\uff1a", None))
        self.tdpi.setText(QCoreApplication.translate("Form", u"0", None))
        self.importButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165", None))
        self.zipButton.setText(QCoreApplication.translate("Form", u"\u538b\u7f29", None))
    # retranslateUi

