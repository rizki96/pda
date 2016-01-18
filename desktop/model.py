import puremvc.patterns.proxy

from components import httpserver


class WebServerProxy(puremvc.patterns.proxy.Proxy):
    NAME = "WebServerProxy"

    def __init__(self, panel, config={'host': '127.0.0.1', 'port': 12345, 'path': '.'},
                 http_root_obj=None, orm_base_obj=None, db_plugin=None):
        super(WebServerProxy, self).__init__(WebServerProxy.NAME, [])
        self._webserver = httpserver.HttpDaemon(panel, config,
                                                http_root_obj=http_root_obj,
                                                orm_base_obj=orm_base_obj,
                                                db_plugin=db_plugin)
        self._webserver.start()

    def tree_mount(self, module_name, http_root, static_dir, orm_base_obj=None, db_plugin=None):
        self._webserver.tree_mount(module_name, http_root, static_dir, orm_base_obj, db_plugin)

    def update_config(self, config):
        self._webserver.config_update(config)

    def stop(self):
        self._webserver.stop()