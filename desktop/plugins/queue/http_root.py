import cherrypy


class QueueHTTPRoot(object):

    @cherrypy.expose
    def index(self):
        return 'QueueHTTPRoot is ready!'