import sys

from PySide6.QtCore import QFile, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox


# 槽函数
def sayhello():
    msgbox = QMessageBox()
    msgbox.setText("Hello world")
    msgbox.setStandardButtons(QMessageBox.Ok)
    ret = msgbox.exec()


class Window:
    def __init__(self):
        super(Window, self).__init__()
        # 从UI文件加载ui
        qfile = QFile("image.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 根据ui定义动态创建相应窗口对象
        self.ui = QUiLoader().load(qfile)
        if not self.ui:
            print(QUiLoader().errorString())
            sys.exit(-1)

        # 信号处理
        self.ui.helloButton.clicked.connect(sayhello)
