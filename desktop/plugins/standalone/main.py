from aside.facade import AsideFacade

import controller


class StandaloneAppFacade(AsideFacade):

    # view
    SHOW_FORM = "showForm"

    # command
    STARTUP = 'startup'

    def __init__(self, multitonKey):
        super(StandaloneAppFacade, self).__init__(multitonKey)

    def initializeFacade(self):
        super(StandaloneAppFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(StandaloneAppFacade, self).initializeController()

        super(StandaloneAppFacade, self).registerCommand(StandaloneAppFacade.STARTUP, controller.StartupCommand)


if __name__ == '__main__':
    pass