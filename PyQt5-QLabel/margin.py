from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout
from PyQt5.Qt import QApplication
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        cental_widget = QWidget(self)
        grid = QGridLayout()

        cental_widget.setLayout(grid)
        self.setCentralWidget(cental_widget)

        label = QLabel()

        label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        label.setText('<u> Метка, на которой написан большой текст, и он переносится на новую строку </u>')

        label.setIndent(50)
        # label.setMargin(50)

        grid.addWidget(label, 0, 0)


if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
