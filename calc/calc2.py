#!/usr/bin/env python3
# Filename: pycalc.py


import sys

from functools import partial


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

__version__ = '0.4'
__author__ = 'Deniel Delamonte'

ERROR_MSG = "ERROR"

# Создаем суб клас для гуи окна
class PyCalcUi(QMainWindow):
    """Гуи"""
    def __init__(self):
       
        super().__init__()
        # параметры главного окна
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        # центраьный виджет
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        #Тут кнопки и дисплей
        self._createDisplay()
        self._createButtons()
	
    def _createDisplay(self):
        """Создаем дисплей."""
        # Дисплейный виджет
        self.display = QLineEdit()
        # Немного параметров
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Добавляем его в разметку.
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Кнопочки"""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # кнопка | положение в сетке
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # содаем кнопки и добавляем их в разметку
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            # давляем разметку кнопок в разметку основную
            self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """текст дисплея."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """получение текста"""
        return self.display.text()

    def clearDisplay(self):
        """очистка текста"""
        self.setDisplayText('')



# обработка данных
def evaluateExpression(expression):
    """оценка выражения."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

# Создание класса контролера для гуи и модели
class PyCalcCtrl:
    """контроллер."""

    def __init__(self, model, view):
        """Инициация контроллер."""
        self._evaluate = model
        self._view = view
        # соиденение котролера и слота
        self._connectSignals()

    def _calculateResult(self):
        """оценка выражения."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """создание выражения."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """соиденение сигналов."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)

# Код клиента
def main():
    """Основные функции."""
    pycalc = QApplication(sys.argv)
    # показываем гуи
    view = PyCalcUi()
    view.show()
    #создается инстанс модели и контроллера
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # И зацыкливаем его.
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()