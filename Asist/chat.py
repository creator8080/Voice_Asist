from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit,QMessageBox,QListWidget,
 QHBoxLayout, QVBoxLayout,QFileDialog,QTextBrowser)
from PyQt5.QtCore import Qt,QTimer 
from PyQt5.QtGui import QPalette,QIcon, QBrush, QPixmap
import sys


app = QApplication([])
main = QWidget()
main.setGeometry(300,200,300,200)
main.setWindowTitle('Python')
row = QHBoxLayout()
row2 = QVBoxLayout()
txt = QLabel('Данил лох')
txt2 = QLabel('Согласен')
timer = QTimer()
timer.setInterval(100)
timer.start()
def update():
    with open('filik.txt','r')as f:
        data = f.read()
    txt.setText(str(data))
    with open('filik2.txt','r')as f:
        data2 = f.read()
    txt2.setText(str(data2))
timer.timeout.connect(update)
row2.addWidget(txt2)
row.addWidget(txt)
row.addLayout(row2)
main.setLayout(row)
main.show()
app.exec_()
