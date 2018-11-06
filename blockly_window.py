#!/usr/bin/env python3




import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QPushButton
import threading
import os


def get_code(webview):
    # print(webview.page())
    # print(dir(webview.page()))
    print(webview.page().runJavaScript("alert($(editor)[0].getCode());"))
    # res = webview.page().mainFrame().evaluateJavaScript()
    # print(res)

x_size = 1366
y_size = 768
class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(x_size, y_size)
        self.setup_ui()


    def setup_ui(self):

        exitAction = QAction(QIcon('editor/a.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)




        self.setMinimumSize(x_size-50, y_size)
        self.setWindowTitle('ESPBlocks')

        self.btn = QPushButton("Run", self)
        self.btn.resize(50, 50)
        self.btn.move(x_size-50, 0)
        self.show()

        self.show()

class WebPage(QWebEnginePage):
    def __init__(self, webview, _event=None):
        super().__init__()
        self.webview = webview
        self._event = _event

    def javaScriptAlert(self, _x, msg):
        self._event(msg)

class BlocklyThread(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.name = "BlocklyThread"
        self.event = event
        self.start()

    def run(self):
        url = 'http://www.micropython.org.cn/pye/editor-en.html#'
        # url = 'file://' + os.path.abspath(os.path.join('blockly','index.html'))
        app = QApplication([])
        editor_window = EditorWindow()

        layout = QVBoxLayout()

        browser = QWebEngineView(editor_window)
        layout.addWidget(browser)
        browser.resize(x_size-50, y_size)
        page = WebPage(browser, self.event)
        browser.setPage(page)

        browser.load(QUrl(url))
        browser.show()

        editor_window.btn.clicked.connect(lambda: get_code(browser))
        sys.exit(app.exec_())


if __name__ == "__main__":
    def print_code(text):
        print("====\n{}\n====".format(text))
    blockly_thread = BlocklyThread(print_code)


