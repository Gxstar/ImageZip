import sys

from PySide6.QtCore import QFile, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QFileDialog, QMainWindow


# 槽函数
def sayhello():
    msgbox = QMessageBox()
    msgbox.setText("Hello world")
    msgbox.setStandardButtons(QMessageBox.Ok)
    ret = msgbox.exec()


def importimage(t):
    path = QFileDialog.getOpenFileName(QMainWindow(), "选择文件", "./", "Image files (*.png *.jpg)")[0]
    pix = QPixmap(path)
    t.ui.picture.setPixmap(pix)


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
        self.ui.importButton.clicked.connect(lambda: importimage(self))
        self.ui.zipButton.clicked.connect(sayhello)
