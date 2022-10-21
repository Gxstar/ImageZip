import sys
from window import Window
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("fav.ico"))
    # app.setStyle(QStyleFactory.create("Fusion"))  # 设置主题风格
    w = Window()
    w.ui.show()
    sys.exit(app.exec())
