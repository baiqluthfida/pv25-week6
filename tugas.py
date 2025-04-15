import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font & Background Adjuster - Baiq Luthfida Khairunnisa F1D022037")
        self.setGeometry(100, 100, 600, 400)

        self.nim = "F1D022037"
        self.name = "Baiq Luthfida Khairunnisa"

        self.font_gray = 0
        self.bg_gray = 255

        self.initUI()

    def initUI(self):

        self.setStyleSheet("background-color: #2e2e2e; color: white;")

        layout = QVBoxLayout()

        self.label = QLabel(self.nim)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.updateLabelColors(font_gray=self.font_gray, bg_gray=self.bg_gray)
        layout.addWidget(self.label)

        layout.addWidget(self.createSliderGroup("Font Size", 20, 60, self.changeFontSize))

        layout.addWidget(self.createSliderGroup("Background Color", 0, 255, self.changeBackgroundColor))

        layout.addWidget(self.createSliderGroup("Font Color", 0, 255, self.changeFontColor))

        identity_label = QLabel(f"Nama: {self.name} | NIM: {self.nim}")
        identity_label.setAlignment(Qt.AlignCenter)
        identity_label.setFont(QFont("Arial", 10))
        layout.addWidget(identity_label)

        self.setLayout(layout)

    def createSliderGroup(self, title, min_val, max_val, slot_func):
        group = QGroupBox(title)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue((min_val + max_val) // 2)
        slider.valueChanged.connect(slot_func)

        h_layout = QHBoxLayout()
        h_layout.addWidget(slider)
        group.setLayout(h_layout)
        group.slider = slider  

        return group

    def changeFontSize(self, value):
        current_font = self.label.font()
        current_font.setPointSize(value)
        self.label.setFont(current_font)

    def changeFontColor(self, value):
        self.font_gray = value
        self.updateLabelColors(font_gray=value, bg_gray=self.bg_gray)

    def changeBackgroundColor(self, value):
        self.bg_gray = value
        self.updateLabelColors(font_gray=self.font_gray, bg_gray=value)

    def updateLabelColors(self, font_gray, bg_gray):
        self.label.setStyleSheet(
            f"color: rgb({font_gray},{font_gray},{font_gray}); "
            f"background-color: rgb({bg_gray},{bg_gray},{bg_gray});"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.show()
    sys.exit(app.exec_())
