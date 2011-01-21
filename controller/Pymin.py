import cherrypy
from lib import template_loader

class controller():
    
    @cherrypy.expose
    def index(self):
	return "aku pymin"
	

    @cherrypy.expose
    def list_vps(self):
	data = ['bram','ganteng','sekali',]
	return template_loader.render('coba.html',data)
	