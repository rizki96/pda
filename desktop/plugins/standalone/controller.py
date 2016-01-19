import os
import sys

import puremvc.patterns.command
import puremvc.interfaces
import logging

from aside.facade import AsideFacade

from . import model

MAIN_APP_KEY = 'mainAppKey'


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):

    def execute(self, note):
        main_panel = note.getBody()
        main_panel.on_shutdown.signal.connect(StartupCommand._on_shutdown)

        self.facade.registerProxy(model.WebServerProxy(main_panel))

    @staticmethod
    def _on_shutdown(event):
        logging.info("standalone: shutdown")
