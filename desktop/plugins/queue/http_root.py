import cherrypy


class QueueRoot(object):

    @cherrypy.expose
    def index(self):
        return 'QueueRoot is ready!'