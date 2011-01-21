import cherrypy 

class controller():
    
    @cherrypy.expose
    def index(self):
	return "ini libpymin"