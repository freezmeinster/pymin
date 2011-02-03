import cherrypy
from lib import template_loader

class Root():
    
    @cherrypy.expose
    def index(self):
	return template_loader.render('login.html')