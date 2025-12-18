# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "certifi==2025.10.5",
#     "charset-normalizer==3.4.4",
#     "idna==3.11",
#     "pillow==10.4.0",
#     "pyqt6==6.10.0",
#     "pyqt6-qt6==6.10.0",
#     "pyqt6-sip==13.10.2",
#     "pyqt6-webengine==6.10.0",
#     "pyqt6-webengine-qt6==6.10.0",
#     "requests==2.32.5",
#     "tkhtmlview==0.3.1",
#     "urllib3==2.5.0",
# ]
# ///

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys



class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Full Python Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Search bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        go_btn = QAction("Go", self)
        go_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(go_btn)

        self.setCentralWidget(self.browser)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
window = Browser()
window.show()
app.exec()
