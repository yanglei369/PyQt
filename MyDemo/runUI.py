# auther: yl
# date: 2022-01-18 11:36
# desciption:
# version: 0.0

import os
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import HorizontalLayout

def main():
    #新建一个主程序
    app = QApplication(sys.argv)
    #新建一个主窗口
    mainWindow = QMainWindow()
    #导入ui
    ui = HorizontalLayout.Ui_MainWindow()
    #外部信息显示在哪个窗口
    ui.setupUi(mainWindow)
    #显示主窗口
    mainWindow.show()
    #退出
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()