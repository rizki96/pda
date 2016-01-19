import os
import sys

import puremvc.patterns.command
import puremvc.interfaces
import logging

from aside.facade import AsideFacade

import model
import utils
from . import http_root, vo

MAIN_APP_KEY = 'mainAppKey'


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):

    def execute(self, note):
        main_panel = note.getBody()
        main_panel.on_shutdown.signal.connect(StartupCommand._on_shutdown)

        main_facade = AsideFacade.getInstance(key=MAIN_APP_KEY)
        web_proxy = main_facade.retrieveProxy(model.WebServerProxy.NAME)
        path = "%s/%s" % (utils.root_dir(), self.facade.PLUGIN_DIR)
        static_dir = '%s/html' % (path,)
        web_proxy.tree_mount(self.facade.PLUGIN_NAME, http_root.QueueHTTPRoot(), static_dir,
                             orm_base_obj=vo.Base,
                             db_plugin=utils.db_str_conn("queue.db", path=path))

    @staticmethod
    def _on_shutdown(event):
        logging.info("queue: shutdown")
