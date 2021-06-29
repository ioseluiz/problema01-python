import sys

from problema01 import Problema01

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton,
                             QLabel,
                             QVBoxLayout,
                             QHBoxLayout,
                             QWidget,
                             QFormLayout,
                             QLineEdit,
                             QDialog
                             )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()
        layout8 = QHBoxLayout()
        layout9 = QHBoxLayout()
        layout10 = QHBoxLayout()
        layout11 = QHBoxLayout()
        layout12 = QHBoxLayout()
        layout13 = QHBoxLayout()
        layout14 = QHBoxLayout()
        layout15 = QHBoxLayout()

        lbl_datos_entrada = QLabel('Datos de Entrada')
        layout.addWidget(lbl_datos_entrada)

        lbl_l1 = QLabel('L1 = ')
        self.txt_l1 = QLineEdit()
        layout1.addWidget(lbl_l1)
        layout1.addWidget(self.txt_l1)
        layout.addLayout(layout1)

        lbl_l2 = QLabel('L2 = ')
        self.txt_l2 = QLineEdit()
        layout2.addWidget(lbl_l2)
        layout2.addWidget(self.txt_l2)
        layout.addLayout(layout2)

        lbl_l3 = QLabel('L3 =')
        self.txt_l3 = QLineEdit()
        layout3.addWidget(lbl_l3)
        layout3.addWidget(self.txt_l3)
        layout.addLayout(layout3)

        lbl_pu = QLabel('Pu =')
        self.txt_pu = QLineEdit()
        layout4.addWidget(lbl_pu)
        layout4.addWidget(self.txt_pu)
        layout.addLayout(layout4)

        lbl_x = QLabel(' X =')
        self.txt_x = QLineEdit()
        layout5.addWidget(lbl_x)
        layout5.addWidget(self.txt_x)
        layout.addLayout(layout5)

        lbl_e = QLabel(' E =')
        self.txt_e = QLineEdit()
        layout6.addWidget(lbl_e)
        layout6.addWidget(self.txt_e)
        layout.addLayout(layout6)

        lbl_i = QLabel(' I =')
        self.txt_i = QLineEdit()
        layout7.addWidget(lbl_i)
        layout7.addWidget(self.txt_i)
        layout.addLayout(layout7)

        lbl_y = QLabel(' Y =')
        self.txt_y = QLineEdit()
        layout12.addWidget(lbl_y)
        layout12.addWidget(self.txt_y)
        layout.addLayout(layout12)

        self.button = QPushButton("Calcular")
        self.button.clicked.connect(self.calcular_problema1)
        layout.addWidget(self.button)

        self.lbl_resultados = QLabel('Resultados')
        layout.addWidget(self.lbl_resultados)

        lbl_ay = QLabel('Ay =')
        self.txt_ay = QLineEdit()
        layout8.addWidget(lbl_ay)
        layout8.addWidget(self.txt_ay)
        layout.addLayout(layout8)

        lbl_by = QLabel('By =')
        self.txt_by = QLineEdit()
        layout9.addWidget(lbl_by)
        layout9.addWidget(self.txt_by)
        layout.addLayout(layout9)

        lbl_cy = QLabel('Cy =')
        self.txt_cy = QLineEdit()
        layout10.addWidget(lbl_cy)
        layout10.addWidget(self.txt_cy)
        layout.addLayout(layout10)

        lbl_dy = QLabel('Dy =')
        self.txt_dy = QLineEdit()
        layout11.addWidget(lbl_dy)
        layout11.addWidget(self.txt_dy)
        layout.addLayout(layout11)

        lbl_m = QLabel('M = ')
        self.txt_m = QLineEdit()
        layout13.addWidget(lbl_m)
        layout13.addWidget(self.txt_m)
        layout.addLayout(layout13)

        lbl_v = QLabel('V = ')
        self.txt_v = QLineEdit()
        layout14.addWidget(lbl_v)
        layout14.addWidget(self.txt_v)
        layout.addLayout(layout14)

        lbl_def = QLabel('Def =')
        self.txt_def = QLineEdit()
        layout15.addWidget(lbl_def)
        layout15.addWidget(self.txt_def)
        layout.addLayout(layout15)
        
        
        

        widget = QWidget()
        widget.setLayout(layout)


        self.setWindowTitle("Problema 01")

        #button = QPushButton("Iniciar")

        self.setCentralWidget(widget)

    def calcular_problema1(self, s):
        solucion = Problema01(self.txt_l1.text(),
                               self.txt_l2.text(),
                               self.txt_l3.text(),
                               self.txt_pu.text(),
                               self.txt_x.text(),
                               self.txt_e.text(),
                               self.txt_i.text(),
                               self.txt_y.text()
                               )
        resultados = solucion.calcular()
        print(resultados)
        ay = round(resultados['ay'],2)
        by = round(resultados['by'],2)
        cy = round(resultados['cy'],2)
        dy = round(resultados['dy'],2)
        momento = round(resultados['M'],2)
        cortante = round(resultados['V'],2)
        deformacion = round(resultados['Def'],2)
        self.txt_ay.setText(str(ay))
        self.txt_by.setText(str(by))
        self.txt_cy.setText(str(cy))
        self.txt_dy.setText(str(dy))
        self.txt_m.setText(str(momento))
        self.txt_v.setText(str(cortante))
        self.txt_def.setText(str(deformacion))






def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()