import sys
import os

# views qt
# from opciones import Ui_select_option

# reconocimiento
from capturandoRostro import *
from entrenandoRF import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView

# request
import requests
# url semilla apiRest
urlApi = 'http://control-personal.test/api/'


class Ui_capturar_win(object):
    def entrenandoModelo(self):
        mainTrainig('Data')
        QMessageBox.about(self.centralwidget, "Realizado", "Procesamiento de imagenes con éxito.")

    def captureUser(self, code):
        print(code)
        savePerson(code, 'Data')
        QMessageBox.about(self.centralwidget, "Bien hecho", "Captura de rostro con éxito.")

    def upListado(self):
        lista = requests.get(urlApi+'lista-empleados')
        empleados = []
        if lista.status_code == 200:
            empleados = lista.json()
            for i in range(self.tabla_empleados.rowCount()):
                self.tabla_empleados.removeRow(0)
        for empleado in empleados:
            self.tabla_empleados.insertRow(self.tabla_empleados.rowCount())
            row = self.tabla_empleados.rowCount() - 1
            self.tabla_empleados.setItem(row, 0, QTableWidgetItem(empleado['cod_empleado']))
            self.tabla_empleados.setItem(row, 1, QTableWidgetItem(empleado['nombres']+' '+empleado['apellidos']))
            self.tabla_empleados.setItem(row, 2, QTableWidgetItem(empleado['cargo']['nombre_cargo']))
            self.tabla_empleados.setItem(row, 3, QTableWidgetItem('Activo' if empleado['estado'] else 'Inactivo'))
            
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setText('Capturar')
            btn.clicked.connect(lambda checked, arg=empleado['cod_empleado']: self.captureUser(arg))
            self.tabla_empleados.setCellWidget(row, 4, btn)

    def setupUi(self, capturar_win):
        capturar_win.setObjectName("capturar_win")
        capturar_win.resize(900, 700)
        capturar_win.setMaximumSize(900, 700)
        capturar_win.setMinimumSize(900, 700)
        capturar_win.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        capturar_win.setStyleSheet("#capturar_win {\n"
"    background-color: #f4f6f9;\n"
"}\n"
"#btn_salir, #btn_entrenar {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(capturar_win)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(20, 10, 89, 25))
        self.btn_salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_salir.setObjectName("btn_salir")

        # salir
        self.btn_salir.clicked.connect(capturar_win.close)
        # end salir

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabla_empleados = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_empleados.setGeometry(QtCore.QRect(10, 90, 880, 580))
        self.tabla_empleados.setObjectName("tabla_empleados")
        self.tabla_empleados.setColumnCount(0)
        self.tabla_empleados.setRowCount(0)

        # table empleados
        self.tabla_empleados.setColumnWidth(5, 10)
        self.tabla_empleados.setColumnCount(5)
        self.tabla_empleados.setHorizontalHeaderLabels(['Código', 'Empleado', 'Cargo', 'Estado', 'Rostro'])
        header = self.tabla_empleados.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # llenado de datos en la tabla de empleados
        self.upListado()
        # end table empleados

        self.btn_entrenar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrenar.setGeometry(QtCore.QRect(730, 30, 161, 41))
        self.btn_entrenar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrenar.setObjectName("btn_entrenar")
        
        # entrenando
        self.btn_entrenar.clicked.connect(self.entrenandoModelo)
        # end entrenando

        capturar_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(capturar_win)
        QtCore.QMetaObject.connectSlotsByName(capturar_win)

    def retranslateUi(self, capturar_win):
        _translate = QtCore.QCoreApplication.translate
        capturar_win.setWindowTitle(_translate("capturar_win", "Lista de empleados"))
        self.btn_salir.setText(_translate("capturar_win", "<- Salir"))
        self.label.setText(_translate("capturar_win", "Empleados"))
        self.btn_entrenar.setText(_translate("capturar_win", "Procesar capturas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    capturar_win = QtWidgets.QMainWindow()
    ui = Ui_capturar_win()
    ui.setupUi(capturar_win)
    capturar_win.show()
    sys.exit(app.exec_())
