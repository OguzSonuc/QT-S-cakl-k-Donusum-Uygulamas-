# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaSayfa

class anaSayfa(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaSayfa()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.hesapla)

    def hesapla(self):
        temp = float (self.ui.lineEdit.text())
        if(self.ui.radioButton_C.isChecked()):
            tempC = temp
            tempF = 9/5*(temp) +32
            tempK = temp +273.15
            self.ui.label_C.setText(str(tempC))
            self.ui.label_F.setText(str(tempF))
            self.ui.label_K.setText(str(tempK))

        elif(self.ui.radioButton_F.isChecked()):
            tempC = (temp -32) /1.80
            tempF = temp
            tempK = 5/9*(temp -32)+273.15
            self.ui.label_C.setText(str(tempC))
            self.ui.label_F.setText(str(tempF))
            self.ui.label_K.setText(str(tempK))

        elif(self.ui.radioButton_K.isChecked()):
            tempC = temp-273.15
            tempF = 9/5 *(temp-273)+32
            tempK = temp
            self.ui.label_C.setText(str(tempC))
            self.ui.label_F.setText(str(tempF))
            self.ui.label_K.setText(str(tempK))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaSayfa()
    widget.show()
    sys.exit(app.exec())
