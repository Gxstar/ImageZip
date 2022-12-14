from sys import exit
from time import sleep
import zip

from PySide6 import QtGui
from PySide6.QtCore import QFile, QFileInfo
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QFileDialog, QMainWindow, QAbstractItemView, QWidget
import ui_image


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        # 从UI文件加载ui
        # qfile = QFile("image.ui")
        # qfile.open(QFile.ReadOnly)
        # qfile.close()
        # 根据ui定义动态创建相应窗口对象
        # self.ui = QUiLoader().load(qfile)
        # if not self.ui:
        #     print(QUiLoader().errorString())
        #     exit(-1)
        ui = ui_image.Ui_Form()
        ui.setupUi(self)
        self.setWindowTitle('图片压缩')

        ui.theight.setValidator(QtGui.QIntValidator(0, 25000))
        ui.twidth.setValidator(QtGui.QIntValidator(0, 25000))
        ui.tsize.setValidator(QtGui.QIntValidator(0, 25000))
        ui.tdpi.setValidator(QtGui.QIntValidator(0, 1500))

        # 槽函数

        # 图片导入
        def import_image():
            paths = QFileDialog.getOpenFileNames(QMainWindow(), "选择文件", "./", "Image files (*.png *.jpg)")[0]
            if len(paths) >= 20:
                QMessageBox.critical(self, "错误", "最大数量不得超过20！")
            else:
                ui.imageList.addItems(paths)
                ui.imageList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # 图片压缩
        def zip_image():
            path_list = ui.imageList.selectedItems()
            if len(path_list) <= 0:
                QMessageBox.critical(self, "错误", "请点击导入后再左侧点击选中要修改的图片！\n（支持按住crtl点击多选）")
            else:
                # QMessageBox.warning(self.ui, "提醒", "请选择压缩后图片保存路径（文件夹）")
                paths = QFileDialog.getExistingDirectory(QMainWindow(), "请选择压缩后图片保存路径")
                for index, i in enumerate(path_list):
                    ui.bar.setValue((index + 1) / len(path_list) * 100)
                    file = i.text()
                    name = QFileInfo(i.text()).baseName()
                    out_file = paths + '/' + name
                    height = int(ui.theight.text())
                    width = int(ui.twidth.text())
                    size = int(ui.tsize.text())
                    dpi = int(ui.tdpi.text())
                    code = zip.image_zip(file, out_file, height, width, size, dpi)
                    sleep(1)
                QMessageBox.information(self, "完成", "压缩完成，请在目标目录查看文件！")

        # 信号处理
        ui.importButton.clicked.connect(import_image)
        ui.zipButton.clicked.connect(zip_image)
