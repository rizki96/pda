import cherrypy


class UserRoot(object):

    @cherrypy.expose
    def index(self):
        return 'UserRoot is ready!'