from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QWidget):

    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.window.setWindowTitle("MiggyBoi Web Browser")

        self.setGeometry(100,60, 1000,800)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.store_btn = QPushButton("Store")
        self.store_btn.setMinimumHeight(30)

        self.zoom_btn = QPushButton("+")
        self.zoom_btn.setMinimumHeight(30)

        self.zout_btn = QPushButton("-")
        self.zout_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.zoom_btn)
        self.horizontal.addWidget(self.zout_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        #self.horizontal.clicked.connect()


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.youtube.com/watch?v=v02KG5S_ESo"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
app.exec_()

'''
Ideas:
- Unregistered web requrest must be changed to:
https://www.google.com/search?q=<invalid request>
which will automatically search it on google

 - Find how to zoom in and out

  - Add loading bar

 - Make it so pressing enter makes a request instead of newline

  - Add play store

 - Find out how to automatically harvest 
'''