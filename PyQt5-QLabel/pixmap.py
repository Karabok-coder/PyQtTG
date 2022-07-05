from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout
from PyQt5.Qt import QApplication
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        cental_widget = QWidget(self)
        grid = QGridLayout()

        cental_widget.setLayout(grid)
        self.setCentralWidget(cental_widget)

        label = QLabel(self)

        pixmap = QtGui.QPixmap('1.png')
        label.setPixmap(pixmap)

        self.resize(pixmap.width(),pixmap.height())

        grid.addWidget(label, 0, 0)

        print(label.pixmap())


if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
