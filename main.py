import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import os

app = QApplication(sys.argv)

# Create a browser window
view = QWebEngineView()

def resource_path(relative_path):
    # checks if the script is running from a PyInstaller executable.
    if getattr(sys, 'frozen', False):
        # PyInstaller puts files in a temporary folder when frozen
        # sys._MEIPASS → the temporary folder where PyInstaller extracts HTML, CSS, JS, etc.
        base_path = sys._MEIPASS
    else:
        # Running normally in Python
        # used when running normally, so it still works outside of an exe.
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


# Load the local HTML file
# html_file = os.path.join(os.path.dirname(__file__), "index.html")
html_file = resource_path("index.html")

view.load(QUrl.fromLocalFile(html_file))

# Show the window
view.show()

sys.exit(app.exec())
