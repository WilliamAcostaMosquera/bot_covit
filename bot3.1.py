# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.setEnabled(True)
        Principal.resize(163, 300)
        Principal.setMaximumSize(QtCore.QSize(163, 300))
        Principal.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Principal.setSizeGripEnabled(True)
        Principal.setModal(False)
        self.formLayout = QtWidgets.QFormLayout(Principal)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Principal)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.correo = QtWidgets.QLineEdit(Principal)
        self.correo.setObjectName("correo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.correo)
        self.label_2 = QtWidgets.QLabel(Principal)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Principal)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nombre = QtWidgets.QLineEdit(Principal)
        self.nombre.setObjectName("nombre")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nombre)
        self.label_4 = QtWidgets.QLabel(Principal)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.documento = QtWidgets.QLineEdit(Principal)
        self.documento.setObjectName("documento")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.documento)
        self.label_5 = QtWidgets.QLabel(Principal)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cargo = QtWidgets.QLineEdit(Principal)
        self.cargo.setObjectName("cargo")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.cargo)
        self.Ejecutar = QtWidgets.QPushButton(Principal)
        self.Ejecutar.setObjectName("Ejecutar")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Ejecutar)
        self.clave = QtWidgets.QLineEdit(Principal)
        self.clave.setTabletTracking(False)
        self.clave.setAutoFillBackground(False)
        self.clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clave.setDragEnabled(False)
        self.clave.setObjectName("clave")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.clave)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Covid-19"))
        self.label.setText(_translate("Principal", "Correo"))
        self.label_2.setText(_translate("Principal", "Clave"))
        self.label_3.setText(_translate("Principal", "Nombre"))
        self.label_4.setText(_translate("Principal", "Documento"))
        self.label_5.setText(_translate("Principal", "Cargo"))
        self.Ejecutar.setText(_translate("Principal", "Ejecutar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QDialog()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
