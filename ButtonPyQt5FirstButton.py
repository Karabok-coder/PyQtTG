from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QApplication, QVBoxLayout


class MaqinWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self);

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        gridVMain = QVBoxLayout(central_widget)

        btn = QPushButton('Моя первая кнопка', central_widget)
        gridVMain.addWidget(btn)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    
    window = MaqinWindow()
    window.show()

    sys.exit(app.exec_())


    
