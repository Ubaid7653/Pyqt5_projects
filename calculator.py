import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        main_layout = QVBoxLayout()

        # Display for showing the calculation
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("""
            background-color: #222222;
            color: #00FFCC;
            font-size: 32px;
            border: 2px solid #555555;
            border-radius: 15px;
            padding-right: 15px;
            padding-left: 10px;
            font-family: 'Arial';
        """)
        main_layout.addWidget(self.display)

        # Grid layout for the buttons
        grid_layout = QGridLayout()

        # Button labels and positions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        # Styles for different buttons
        number_button_style = """
            QPushButton {
                background-color: #333333;
                color: #FFFFFF;
                font-size: 22px;
                font-family: 'Arial';
                border: 2px solid #444444;
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """

        operator_button_style = """
            QPushButton {
                background-color: #FF9500;
                color: #FFFFFF;
                font-size: 22px;
                font-family: 'Arial';
                border: 2px solid #e67e00;
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #ffad33;
            }
            QPushButton:pressed {
                background-color: #cc7a00;
            }
        """

        special_button_style = """
            QPushButton {
                background-color: #FF3B30;
                color: #FFFFFF;
                font-size: 22px;
                font-family: 'Arial';
                border: 2px solid #d6302b;
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #ff6050;
            }
            QPushButton:pressed {
                background-color: #cc3227;
            }
        """

        # Add buttons to the grid layout
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(90, 90)
            # Apply different styles for numbers, operators, and special buttons
            if text.isdigit() or text == '.':
                button.setStyleSheet(number_button_style)
            elif text in ['/', '*', '-', '+', '=']:
                button.setStyleSheet(operator_button_style)
            elif text == 'C':
                button.setStyleSheet(special_button_style)

            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)

        # Set the main layout
        self.setLayout(main_layout)
        self.setWindowTitle("Professional Calculator")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #1c1c1c;")

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == 'C':
            # Clear the display
            self.display.clear()
        elif button_text == '=':
            # Evaluate the expression
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            # Append the button text to the display
            self.display.setText(self.display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
