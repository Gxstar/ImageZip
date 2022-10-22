# 图片压缩工具

用python写的一个图片压缩工具，功能很简单，主要是为了学习pyside图形化编程。

系统环境：
- 操作系统：Windows11 22H2
- Python：3.9

Python包：
- Pillow>=9.2.0
- PySide6>=6.4.0

打包工具：
- Nuitka>=1.1.6

打包命令
```commandline
nuitka --onefile --standalone --output-dir=out --windows-icon-from-ico=fav.ico --windows-disable-console --enable-plugin=pyside6 main.py
```

