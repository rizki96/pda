import cherrypy


class MainHttpRoot(object):
    @cherrypy.expose
    def index(self):
        return "MainHttpRoot is ready!"


