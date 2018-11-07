#!/usr/bin/env python3

import sys
from PyQt5.QtCore import QUrl, QCoreApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QWidget
import threading


x_size = 1366
y_size = 768
class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(x_size, y_size)
        self.setup_ui()


    def setup_ui(self):
        self.setMinimumSize(x_size-50, y_size)
        self.setWindowTitle('ESPBlocks')

        self.btn = QPushButton("Run", self)
        self.btn.resize(50, 50)
        self.btn.move(x_size-50, 0)

        self.show()

class WebView(QWebEngineView):

    def bind_event(self, event):
        self._event = event

    def get_code_callback(self, result):
        print(result)
        self._event(result)

    def get_code(self):
        self.page().runJavaScript("($(editor)[0].getCode());", self.get_code_callback)
        # print(res)

class BlocklyThread(threading.Thread):

    def __init__(self, event, name="BlocklyThread"):
        super().__init__()
        self.name = name
        self.event = event
        self.start()

    def run(self):
        app = QApplication([])

        layout = QVBoxLayout()
        editor_window = EditorWindow()
        browser = WebView(editor_window)
        browser.bind_event(self.event)
        editor_window.btn.clicked.connect(lambda: browser.get_code())
        layout.addWidget(browser)

        browser.resize(x_size-50, y_size)

        url = 'http://www.micropython.org.cn/pye/editor-en.html#'
        browser.load(QUrl(url))
        browser.show()
        app.exec_()
        browser.close()
        browser.destroy()
        editor_window.close()

if __name__ == "__main__":
    # app = QApplication([])
    def print_code(text):
        print("====\n{}\n====".format(text))
    blockly_thread = BlocklyThread(print_code)



