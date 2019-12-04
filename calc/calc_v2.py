import sys

# 1 Далее всякое из PyQt для виджета

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2  Так а тут инстанса Qapliction
app = QApplication(sys.argv)

# 3 Так терь тут параметры окна апликухи, гуи.

window = QWidget()
window.setWindowTitle('Calculator')
window.setGeometry(100, 100, 200, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hell no!</h1>', parent=window)
helloMsg.move(60, 15)

# 4. показать гуи
window.show()

# 5. и запустить его в луп....
sys.exit(app.exec_())