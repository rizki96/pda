import cherrypy


class UserHTTPRoot(object):

    @cherrypy.expose
    def index(self):
        return 'UserHTTPRoot is ready!'