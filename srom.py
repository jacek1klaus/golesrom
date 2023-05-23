from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create a web view widget
        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        # Create a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Create navigation actions
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.webview.back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.webview.forward)
        toolbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.webview.reload)
        toolbar.addAction(reload_btn)

        # Create the URL input field
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.load_url)
        toolbar.addWidget(self.url_input)

        # Load a default URL
        self.load_url(QUrl("https://www.google.com"))

    def load_url(self, url):
        # Load the given URL
        self.webview.load(url)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Set the style to a platform-specific style
    app.setStyle("Fusion")

    # Create the web browser window
    browser = WebBrowser()
    browser.show()

    # Execute the application's event loop
    sys.exit(app.exec_())
