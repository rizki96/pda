__author__ = 'rizki'

import os
import sys
import yaml
import importlib
import logging

from uuid import getnode as get_mac
import puremvc.patterns.command
import puremvc.interfaces

from time import sleep
from aside import pages, hooks, events

import view
import model
import main
import http_root
import vo
import utils


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):

    def execute(self, note):
        main_panel = note.getBody()

        # first running the webserver
        self.facade.registerProxy(model.WebServerProxy(main_panel,
                                                       config={'host': '127.0.0.1', 'port': 12345,
                                                               #'path': '%s/ui/html' % utils.root_dir()
                                                               'path': None,
                                                                },
                                                       http_root_obj=http_root.MainHttpRoot(),
                                                       orm_base_obj=vo.Base,
                                                       db_plugin=utils.db_str_conn('mainapp.db')),)

        with open('%s/plugins.yaml' % utils.root_dir()) as stream:
            cfg = yaml.safe_load(stream)
            if cfg:
                # register startup class
                for key,val in cfg.iteritems():
                    try:
                        plugin_facade_cls = utils.class_for_name(val['module'] + '.main', 'PluginFacade')
                        facade = plugin_facade_cls.getInstance(key=key)
                        if facade:
                            logging.info('%s: plugin loaded' % key)
                            facade.module_name = key
                        # calling startup
                        facade.sendNotification(facade.STARTUP, main_panel)
                    except Exception, e:
                        logging.info('%s: %s' % (key, e.message))

        # must be register or else script won't be loaded
        pages.register_file("main", "%s/ui/html/main.html" % utils.root_dir())
        # NOTE: the statics will not being used in main
        #pages.register_url("main", "http://localhost:12345/statics/index.html")

        main_panel.on_shutdown.signal.connect(StartupCommand._on_shutdown)
        main_form = view.MainFormMediator(main_panel.ui)

        self.facade.registerMediator(main_form)

        hooks.register_object("main_form", main_form)

        events.register_signal("error_message")

    @staticmethod
    def _on_shutdown(event):
        logging.info('main: shutdown')
        facade = main.MainAppFacade.getInstance("mainAppKey")
        #wp_obj = facade.retrieveProxy(model.WebParseProxy.NAME)
        #if wp_obj:
        #    wp_obj.__deinit__()  # must quit browser
        ws_obj = facade.retrieveProxy(model.WebServerProxy.NAME)
        if ws_obj:
            ws_obj.stop()
