from PySide import QtGui

# Cria a aplicacao na memoria
app = QtGui.QApplication([])

# Configura a janela de login
loginwindow = QtGui.QDialog()
loginwindow.show()
loginwindow.setWindowTitle("Bemvindo Dora Louca")
login_layout = QtGui.QGridLayout()
loginwindow.setLayout(login_layout)

# Configura a label Usuario
labeluser = QtGui.QLabel()
labeluser.setText("Usuario")
login_layout.addWidget(labeluser)

# Configura a label Senha
labelsenha = QtGui.QLabel()
labelsenha.setText("Senha")
login_layout.addWidget(labelsenha)

# Executa a aplicacao
app.exec_()