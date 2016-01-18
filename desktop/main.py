__author__ = 'rizki'

from PySide import QtGui
from aside.facade import AsideFacade

import sys
import controller
import components


class MainAppFacade(AsideFacade):

    # view
    SHOW_FORM = "showForm"

    # command
    STARTUP = 'startup'

    def __init__(self, multitonKey):
        super(MainAppFacade, self).__init__(multitonKey)

    def initializeFacade(self):
        super(MainAppFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(MainAppFacade, self).initializeController()

        super(MainAppFacade, self).registerCommand(MainAppFacade.STARTUP, controller.StartupCommand)


if __name__ == '__main__':
    qtapp = QtGui.QApplication(sys.argv)

    main_app = MainAppFacade.getInstance(key='mainAppKey')

    # NOTE: remember to disable webview QURL open
    main_window = components.QtMainWindow()
    main_window.show()

    main_app.sendNotification(MainAppFacade.STARTUP, main_window)

    sys.exit(qtapp.exec_())
