from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.Qt import QApplication
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        label = QLabel('Мой первый виджет')
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.setWindowTitle('Прогграмма с Qlabel')
        self.resize(300, 150)

        self.setCentralWidget(label)

if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

