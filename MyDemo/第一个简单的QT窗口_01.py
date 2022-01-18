import sys
from PyQt5.QtWidgets import  QApplication,QWidget


if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口尺寸
    w.resize(300,150)
    #移动窗口
    w.move(300,300)

    #设置窗口标题
    w.setWindowTitle("pyqt5-01")
    
    #显示窗口
    w.show()

    #主循环
    sys.exit(app.exec_())