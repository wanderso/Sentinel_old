from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)



class BaseApplication(QApplication):
    pass


class RootWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.view_selector_panel = ViewSelectorPanel(self)
        self.view_action_panel = ViewActionPanel(self)

        self.layout.addWidget(self.view_selector_panel)
        self.layout.addWidget(self.view_action_panel)
        self.setLayout(self.layout)
        self.show()

    def main_menu_signal(self):
        self.view_action_panel.display_main_menu()


class ViewSelectorPanel(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.settings_menu_button = QPushButton('Main Menu')
        self.scene_menu_button = QPushButton('Current Scene')
        self.layout.addWidget(self.settings_menu_button)
        self.layout.addWidget(self.scene_menu_button)

        self.settings_menu_button.clicked.connect(self.parent().main_menu_signal)

        self.setLayout(self.layout)
        self.show()

class ViewActionPanel(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.text_pane = QTextEdit(self)
        self.layout.addWidget(self.text_pane)
        self.setLayout(self.layout)
        self.show()

    def display_main_menu(self):
        self.set_text_in_pane("Main menu")

    def set_text_in_pane(self, text):
        self.text_pane.setHtml(text)





if __name__ == "__main__":
    BA = BaseApplication([])
    window = RootWindow()
    BA.exec_()

