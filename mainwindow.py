from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit
from simpleeval import simple_eval


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting window title and size
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Instantiation of the Main Widget
        self.central_widget = MainWidget()

        # Setting the central widget of the Main window
        self.setCentralWidget(self.central_widget)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Definition of Layout
        main_layout = QVBoxLayout(self)

        # Instantiation of the Holder Widget that holds all the layers
        self.layout_holder = HorizontalLayoutsHolder()

        # Adding the Holder Widget to the layout
        main_layout.addWidget(self.layout_holder)


class HorizontalLayoutsHolder(QWidget):
    def __init__(self):
        super().__init__()

        # Definition of Layout
        self.layout = QVBoxLayout(self)

        # Defining line_edit object + adding it to the layout
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

        # Instantiating the layer objects + passing a reference to the line_edit inside this class
        layer_zero = LayerZero(self.line_edit)
        layer_one = LayerOne(self.line_edit)
        layer_two = LayerTwo(self.line_edit)
        layer_three = LayerThree(self.line_edit)
        layer_four = LayerFour(self.line_edit)

        # Adding the elements(Layers of Buttons) to the layout
        self.layout.addWidget(layer_zero)
        self.layout.addWidget(layer_one)
        self.layout.addWidget(layer_two)
        self.layout.addWidget(layer_three)
        self.layout.addWidget(layer_four)


class LayerZero(QWidget):
    def __init__(self, line_edit):
        super().__init__()

        # Passing by reference (this is the same QlineEdit in the HorizontalLayoutsHolder class)
        self.line_edit = line_edit

        # Definition of Layout
        self.layout = QHBoxLayout(self)

        # Definition of buttons
        self.C_button = QPushButton("C")
        self.CE_button = QPushButton("CE")
        self.modulo_button = QPushButton("%")
        self.divide_button = QPushButton("/")

        # Adding the elements(buttons) to the layout
        self.layout.addWidget(self.C_button)
        self.layout.addWidget(self.CE_button)
        self.layout.addWidget(self.modulo_button)
        self.layout.addWidget(self.divide_button)

        # Assigning button signals to the slots
        self.C_button.clicked.connect(self.C_clicked)
        self.CE_button.clicked.connect(self.CE_clicked)
        self.modulo_button.clicked.connect(self.modulo_clicked)
        self.divide_button.clicked.connect(self.divide)

    # slots/button functions

    def C_clicked(self):
        self.line_edit.clear()

    def CE_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text[:-1])

    def modulo_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "%")

    def divide(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "/")


class LayerOne(QWidget):
    def __init__(self, line_edit):
        super().__init__()

        self.line_edit = line_edit

        # Definition of Layout
        self.layout = QHBoxLayout(self)

        # Definition of buttons
        self.seven_button = QPushButton("7")
        self.eight_button = QPushButton("8")
        self.nine_button = QPushButton("9")
        self.multiply_button = QPushButton("*")

        # Adding the elements(buttons) to the layout
        self.layout.addWidget(self.seven_button)
        self.layout.addWidget(self.eight_button)
        self.layout.addWidget(self.nine_button)
        self.layout.addWidget(self.multiply_button)

        # Assigning button signals to the slots
        self.seven_button.clicked.connect(self.seven_clicked)
        self.eight_button.clicked.connect(self.eight_clicked)
        self.nine_button.clicked.connect(self.nine_clicked)
        self.multiply_button.clicked.connect(self.multiply_clicked)

    # slots/button functions

    def seven_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "7")

    def eight_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "8")

    def nine_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "9")

    def multiply_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "*")


class LayerTwo(QWidget):
    def __init__(self, line_edit):
        super().__init__()

        self.line_edit = line_edit

        # Definition of Layout
        self.layout = QHBoxLayout(self)

        # Definition of buttons
        self.four_button = QPushButton("4")
        self.five_button = QPushButton("5")
        self.six_button = QPushButton("6")
        self.plus_button = QPushButton("+")

        # Adding the elements(buttons) to the layout
        self.layout.addWidget(self.four_button)
        self.layout.addWidget(self.five_button)
        self.layout.addWidget(self.six_button)
        self.layout.addWidget(self.plus_button)

        # Assigning button signals to the slots
        self.four_button.clicked.connect(self.four_clicked)
        self.five_button.clicked.connect(self.five_clicked)
        self.six_button.clicked.connect(self.six_clicked)
        self.plus_button.clicked.connect(self.plus_clicked)

    # slots/button functions

    def four_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "4")

    def five_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "5")

    def six_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "6")

    def plus_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "+")


class LayerThree(QWidget):
    def __init__(self, line_edit):
        super().__init__()

        self.line_edit = line_edit

        # Definition of Layout
        self.layout = QHBoxLayout(self)

        # Definition of buttons
        self.one_button = QPushButton("1")
        self.two_button = QPushButton("2")
        self.three_button = QPushButton("3")
        self.minus_button = QPushButton("-")

        # Adding the elements(buttons) to the layout
        self.layout.addWidget(self.one_button)
        self.layout.addWidget(self.two_button)
        self.layout.addWidget(self.three_button)
        self.layout.addWidget(self.minus_button)

        # Assigning button signals to the slots
        self.one_button.clicked.connect(self.one_clicked)
        self.two_button.clicked.connect(self.two_clicked)
        self.three_button.clicked.connect(self.three_clicked)
        self.minus_button.clicked.connect(self.minus_clicked)

    # slots/button functions

    def one_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "1")

    def two_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "2")

    def three_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "3")

    def minus_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "-")


class LayerFour(QWidget):
    def __init__(self, line_edit):
        super().__init__()

        self.line_edit = line_edit

        # Definition of Layout
        self.layout = QHBoxLayout(self)

        # Definition of buttons
        self.zero_button = QPushButton("0")
        self.point_button = QPushButton(".")
        self.equals_button = QPushButton("=")

        # Adding the elements(buttons) to the layout
        self.layout.addWidget(self.zero_button)
        self.layout.addWidget(self.point_button)
        self.layout.addWidget(self.equals_button)

        # Assigning button signals to the slots
        self.zero_button.clicked.connect(self.zero_clicked)
        self.point_button.clicked.connect(self.point_clicked)
        self.equals_button.clicked.connect(self.equals_clicked)

    # slots/button functions
    def zero_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + "0")

    def point_clicked(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + ".")

    def equals_clicked(self):
        current_text = self.line_edit.text()
        result = simple_eval(current_text)
        self.line_edit.setText(str(result))
