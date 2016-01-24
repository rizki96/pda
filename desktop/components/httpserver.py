__author__ = 'rizki'

from PySide import QtCore

import os
import cherrypy
from cp_sqlalchemy import SQLAlchemyTool, SQLAlchemyPlugin

HOST, PORT = '127.0.0.1', 12345


class HttpDaemon(QtCore.QThread):

    def __init__(self, panel, config={'host': HOST, 'port': PORT, 'path': '.'},
                 http_root_obj=None, orm_base_obj=None, db_plugin=None):
        super(HttpDaemon, self).__init__(panel)
        self._config = config
        self._http_root = http_root_obj
        self._orm_base = orm_base_obj
        self._db_plugin = db_plugin

    def run(self):
        root = self._http_root
        self.tree_mount('', root, self._config['path'], orm_base_obj=self._orm_base, db_plugin=self._db_plugin)
        cherrypy.config.update({'server.socket_host': self._config['host'],
                                'server.socket_port': self._config['port']})
        cherrypy.engine.start()
        cherrypy.engine.block()

    def tree_mount(self, module_name, http_root, static_dir, orm_base_obj=None, db_plugin=None):  # db sqlite
        if http_root:
            base_uri = '/%s' % module_name
            config_map = {}
            if static_dir:
                config_map = {
                    '/statics': {
                        'tools.staticdir.on': True,
                        'tools.staticdir.dir': static_dir,
                        'tools.staticdir.index': 'index.html',
                    },
                }
            if orm_base_obj and db_plugin:
                cherrypy.tools.db = SQLAlchemyTool()
            config_map.update({
                '/': {
                    'tools.db.on': True if orm_base_obj and db_plugin else False
                }
            })
            cherrypy.tree.mount(http_root, base_uri, config_map)
            if orm_base_obj and db_plugin:
                sqlalchemy_plugin = SQLAlchemyPlugin(
                    cherrypy.engine, orm_base_obj, db_plugin,
                    echo=True
                )
                sqlalchemy_plugin.subscribe()
                sqlalchemy_plugin.create()

    def config_update(self, config):
        cherrypy.config.update(config)

    def stop(self):
        cherrypy.engine.exit()
        if not self.wait(5000):
            self.terminate()
            self.wait()
