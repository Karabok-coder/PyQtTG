from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QFormLayout, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.Qt import QApplication
from PyQt5 import QtCore
from scipy.misc import central_diff_weights

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        cental_widget = QWidget()
        self.setCentralWidget(cental_widget)

        nameLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QLineEdit()

        nameLabel = QLabel(self.tr("Name:"))
        nameLabel.setBuddy(nameLineEdit)

        emailLabel = QLabel(self.tr("Name:"))
        emailLabel.setBuddy(emailLineEdit)

        ageLabel = QLabel(self.tr("Name:"))
        ageLabel.setBuddy(ageSpinBox)

        grid = QGridLayout()

        grid.addWidget(nameLineEdit, 0, 1)
        grid.addWidget(emailLineEdit, 1, 1)
        grid.addWidget(ageSpinBox, 2, 1)

        grid.addWidget(nameLabel, 0, 0)
        grid.addWidget(emailLabel, 1, 0)
        grid.addWidget(ageLabel, 2, 0)

        cental_widget.setLayout(grid)


if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
