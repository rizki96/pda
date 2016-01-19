import importlib
from aside.facade import AsideFacade

from . import controller


def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


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