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

        formLayout = QFormLayout()
        formLayout.addRow(nameLabel, nameLineEdit)
        formLayout.addRow(emailLabel, emailLineEdit)
        formLayout.addRow(ageLabel, ageSpinBox)
        cental_widget.setLayout(formLayout)

if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
