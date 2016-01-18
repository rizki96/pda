__author__ = 'rizki'

import logging

from PySide import QtCore, QtGui, QtWebKit
from PySide.QtCore import QObject, Signal
from ui import main_window
#from ui import web_form
from aside import components

def centerCoord(parent, WIDTH=640, HEIGHT=480):
    desktop = parent
    screen_width = desktop.width()
    screen_height = desktop.height()
    if WIDTH > screen_width: WIDTH = screen_width
    if HEIGHT > screen_height: HEIGHT = screen_height
    x = (screen_width - WIDTH) / 2
    y = (screen_height - HEIGHT) / 2
    return (x,y,WIDTH,HEIGHT)


class ShutdownSignal(QObject):
    signal = Signal(QObject)


class QtMainWindow(QtGui.QMainWindow):

    widget = {}

    def __init__(self, parent=None):
        super(QtMainWindow, self).__init__(parent, QtCore.Qt.WindowModal)
        #self.ui = main_window.Ui_MainWindow()
        #self.ui.setupUi(self)
        self.ui = self.create_ui_form()
        #self.ui.mdiArea.addSubWindow(self.create_form(), QtCore.Qt.FramelessWindowHint)
        #self.ui.mdiArea.addSubWindow(self.create_form())
        x, y, width, height = centerCoord(QtGui.QApplication.desktop(), 1024, 680)
        self.setGeometry(x, y, width, height)
        self.on_shutdown = ShutdownSignal()

    def create_ui_form(self):
        ui = main_window.Ui_MainWindow()
        ui.setupUi(self)
        for attr in [
                QtWebKit.QWebSettings.AutoLoadImages,
                QtWebKit.QWebSettings.JavascriptEnabled,
                QtWebKit.QWebSettings.JavaEnabled,
                QtWebKit.QWebSettings.PluginsEnabled,
                QtWebKit.QWebSettings.JavascriptCanOpenWindows,
                QtWebKit.QWebSettings.JavascriptCanAccessClipboard,
                QtWebKit.QWebSettings.DeveloperExtrasEnabled,
                QtWebKit.QWebSettings.SpatialNavigationEnabled,
                QtWebKit.QWebSettings.OfflineStorageDatabaseEnabled,
                QtWebKit.QWebSettings.OfflineWebApplicationCacheEnabled,
                QtWebKit.QWebSettings.LocalStorageEnabled,
                QtWebKit.QWebSettings.LocalStorageDatabaseEnabled,
                QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls,
                QtWebKit.QWebSettings.LocalContentCanAccessFileUrls,
        ]:
            #QtWebKit.QWebSettings.globalSettings().setAttribute(attr, True)
            ui.webView.page().settings().setAttribute(attr, True)
        ui.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        ui.webView.setPage(components.WebPage())
        return ui

    def closeEvent(self, event):
        self.on_shutdown.signal.emit(event)

'''
    def create_form(self):
        self.form_ui = web_form.Ui_WebForm()
        form_widget = QtGui.QWidget()
        for attr in [
                QtWebKit.QWebSettings.AutoLoadImages,
                QtWebKit.QWebSettings.JavascriptEnabled,
                QtWebKit.QWebSettings.JavaEnabled,
                QtWebKit.QWebSettings.PluginsEnabled,
                QtWebKit.QWebSettings.JavascriptCanOpenWindows,
                QtWebKit.QWebSettings.JavascriptCanAccessClipboard,
                QtWebKit.QWebSettings.DeveloperExtrasEnabled,
                QtWebKit.QWebSettings.SpatialNavigationEnabled,
                QtWebKit.QWebSettings.OfflineStorageDatabaseEnabled,
                QtWebKit.QWebSettings.OfflineWebApplicationCacheEnabled,
                QtWebKit.QWebSettings.LocalStorageEnabled,
                QtWebKit.QWebSettings.LocalStorageDatabaseEnabled,
                QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls,
                QtWebKit.QWebSettings.LocalContentCanAccessFileUrls,
        ]:
            QtWebKit.QWebSettings.globalSettings().setAttribute(attr, True)
        self.form_ui.setupUi(form_widget)
        self.form_ui.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.form_ui.webView.setPage(components.WebPage())
        return form_widget
'''
