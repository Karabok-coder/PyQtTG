from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QPushButton
from PyQt5.Qt import QApplication
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        cental_widget = QWidget(self)
        grid = QGridLayout()

        cental_widget.setLayout(grid)
        self.setCentralWidget(cental_widget)

        self.label = QLabel('Мой первый виджет')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        btn = QPushButton('Вывести выделенный текст')
        btn.clicked.connect(self.btn_alig)
        
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(btn, 1, 0)

    def btn_alig(self):
        print(self.label.selectedText())

if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

