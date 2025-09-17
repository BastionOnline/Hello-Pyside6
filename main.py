import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import os

app = QApplication(sys.argv)

# Create a browser window
view = QWebEngineView()

# Load the local HTML file
html_file = os.path.join(os.path.dirname(__file__), "index.html")
view.load(QUrl.fromLocalFile(html_file))

# Show the window
view.show()

sys.exit(app.exec())
