import sys
import os
import webbrowser
# views qt
from capturar import Ui_capturar_win
from browser import Ui_browser_win

# reconocimiento
# from capturandoRostro import *
# from entrenandoRF import *
from reconocimientoDeRostro import *

# from PySide2 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView

import banner_rc
import images_rc

class Ui_select_option(object):

    ''' Funciones de la app '''
    # init browser
    def openAsistsCode(self):
        webbrowser.get('firefox').open_new('http://control-personal.test/marcar-asistencia')
    
    # init browser
    def openAdmin(self):
        # self.windowNavegador = QtWidgets.QMainWindow()
        # self.ui = Ui_browser_win()
        # self.ui.setupUi(self.windowNavegador)
        # self.windowNavegador.show()

        webbrowser.get('firefox').open_new('http://control-personal.test')

    # iniciar reconocimiento
    def iniciarReconocimiento(self):
        mainRecognition('Data')
    
    # listar usuarios
    def openListaUsuarios(self):
        self.windowCapturar = QtWidgets.QMainWindow()
        self.ui = Ui_capturar_win()
        self.ui.setupUi(self.windowCapturar)
        self.windowCapturar.show()

    # main application
    def setupUi(self, select_option):
        select_option.setObjectName("select_option")
        select_option.resize(737, 555)
        select_option.setMaximumSize(737, 555)
        select_option.setMinimumSize(737, 555)
        select_option.setStyleSheet("#select_option {\n"
"    background-color: #f4f6f9;\n"
"}\n"
"#btn_reconocimiento, #btn_capturar, #btn_admin,#btn_codigo {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"    border-radius: 4px;\n"
"}")
        self.label_2 = QtWidgets.QLabel(select_option)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 751, 581))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/banner.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(select_option)
        self.label.setGeometry(QtCore.QRect(260, 60, 261, 141))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/logo.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(select_option)
        self.widget.setGeometry(QtCore.QRect(170, 240, 411, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_reconocimiento = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reconocimiento.setFont(font)
        self.btn_reconocimiento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reconocimiento.setObjectName("btn_reconocimiento")
        # iniciar reconocimiento
        self.btn_reconocimiento.clicked.connect(self.iniciarReconocimiento)
        # end iniciar reconocimiento
        self.verticalLayout.addWidget(self.btn_reconocimiento)

        self.btn_codigo = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_codigo.setFont(font)
        self.btn_codigo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_codigo.setObjectName("btn_codigo")
        # iniciar asistencia por codigo
        self.btn_codigo.clicked.connect(self.openAsistsCode)
        # end iniciar asistencia por codigo
        self.verticalLayout.addWidget(self.btn_codigo)

        self.btn_capturar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_capturar.setFont(font)
        self.btn_capturar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_capturar.setObjectName("btn_capturar")
        # iniciar captura
        self.btn_capturar.clicked.connect(self.openListaUsuarios)
        # self.btn_capturar.clicked.connect(select_option.close)
        # end iniciar captura

        self.verticalLayout.addWidget(self.btn_capturar)
        self.btn_admin = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_admin.setFont(font)
        self.btn_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_admin.setObjectName("btn_admin")
        # panel admin
        self.btn_admin.clicked.connect(self.openAdmin)
        # self.btn_admin.clicked.connect(select_option.close)
        # end panel admin

        self.verticalLayout.addWidget(self.btn_admin)

        self.retranslateUi(select_option)
        QtCore.QMetaObject.connectSlotsByName(select_option)

    def retranslateUi(self, select_option):
        _translate = QtCore.QCoreApplication.translate
        select_option.setWindowTitle(_translate("select_option", "Form"))
        self.btn_reconocimiento.setText(_translate("select_option", "Asistencia por cámara"))
        self.btn_codigo.setText(_translate("select_option", "Asistencia por código"))
        self.btn_capturar.setText(_translate("select_option", "Capturar Rostro"))
        self.btn_admin.setText(_translate("select_option", "Administrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_option = QtWidgets.QWidget()
    ui = Ui_select_option()
    ui.setupUi(select_option)
    select_option.show()
    sys.exit(app.exec_())
