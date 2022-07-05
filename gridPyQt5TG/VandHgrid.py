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

        Vlayout_1 = QVBoxLayout()
        Vlayout_2 = QVBoxLayout()
        Vlayout_3 = QVBoxLayout()

        Vlayout_1.addWidget(nameLabel)
        Vlayout_1.addWidget(nameLineEdit)
        
        Vlayout_2.addWidget(ageLabel)
        Vlayout_2.addWidget(ageSpinBox)
        
        Vlayout_3.addWidget(emailLabel)
        Vlayout_3.addWidget(emailLineEdit)
        
        HboxLayout = QHBoxLayout()

        HboxLayout.addLayout(Vlayout_1)
        HboxLayout.addLayout(Vlayout_2)
        HboxLayout.addLayout(Vlayout_3)
        
        cental_widget.setLayout(HboxLayout)

if __name__ == "__main__":
    import sys

    app = QApplication([]) # QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
