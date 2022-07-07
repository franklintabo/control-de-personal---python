from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_browser_win(object):
    def setupUi(self, browser_win):
        browser_win.setObjectName("browser_win")
        browser_win.resize(1400, 900)
        browser_win.setMaximumSize(1400, 900)
        browser_win.setMinimumSize(1400, 900)
        browser_win.setStyleSheet("#browser_win {\n"
"    background-color: #f4f6f9;\n"
"}\n"
"#btn_salir {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(browser_win)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(20, 20, 89, 25))
        self.btn_salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_salir.setObjectName("btn_salir")

        # salir
        self.btn_salir.clicked.connect(browser_win.close)
        # end salir

        self.cont_navegador = QtWidgets.QWidget(self.centralwidget)
        self.cont_navegador.setGeometry(QtCore.QRect(0, 60, 1400, 900))
        self.cont_navegador.setMinimumSize(QtCore.QSize(971, 0))
        self.cont_navegador.setObjectName("cont_navegador")

        # view browser
        self.browser = QWebEngineView(self.cont_navegador)
        self.browser.setUrl(QUrl("http://control-personal.test"))
        # self.browser.setGeometry(QtCore.QRect(10, 0, 1071, 791))
        self.browser.setGeometry(0, 0, 1400, 900)
        # end view browser
        
        browser_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(browser_win)
        QtCore.QMetaObject.connectSlotsByName(browser_win)

    def retranslateUi(self, browser_win):
        _translate = QtCore.QCoreApplication.translate
        browser_win.setWindowTitle(_translate("browser_win", "Panel admin"))
        self.btn_salir.setText(_translate("browser_win", "<- Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    browser_win = QtWidgets.QMainWindow()
    ui = Ui_browser_win()
    ui.setupUi(browser_win)
    browser_win.show()
    sys.exit(app.exec_())
