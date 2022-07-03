from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QApplication

class MainWindow(QMainWindow):
    def __iinit__(self):
        super.__init__(self)

if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
