from aside.facade import AsideFacade

import controller


class PluginFacade(AsideFacade):

    STARTUP = 'startup'
    PLUGIN_DIR = "plugins/user"

    def __init__(self, multitonKey):
        super(PluginFacade, self).__init__(multitonKey)

    def initializeFacade(self):
        super(PluginFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(PluginFacade, self).initializeController()

        super(PluginFacade, self).registerCommand(PluginFacade.STARTUP, controller.StartupCommand)


if __name__ == '__main__':
    pass