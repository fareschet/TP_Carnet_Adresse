from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow)
import sys
from Vue.FenetreCarnetAdresse import FenetreCarnetAdresse

icon_path = "images/background.jpg"
app = QApplication(sys.argv)
MainWindow = QMainWindow()
MainWindow.setWindowIcon(QIcon(icon_path))
ui = FenetreCarnetAdresse()
ui.setupUi(MainWindow)
style_css = "Vue/style.css"
with open(style_css, "r") as f:
    app.setStyleSheet(f.read())
MainWindow.show()
sys.exit(app.exec())