from PyQt5.QtWidgets import *

app = QApplication

window = QWidget()

lil = ALable()
#доробити


lbl = QLabl("Скільки буде 2+2")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")

main_line = QWBoxLayout()
main_line.addWidget(lbl)


h1 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)

mail_line.addLayout(h1)

def true_var_1
    msg = QMessageBox()
    msg.swtText("Правильно!")
    msg.exec()

    ans1.clicked.connect(true_var_1)



window.setLayout(main_line)
window.show()
app.exec()