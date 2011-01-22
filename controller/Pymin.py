import cherrypy,os
from lib import template_loader,setting,item
from models import *

class controller():
    
    @cherrypy.expose
    def index(self):
        vps = vps_info.list_vps()
	data = { 'nama' : 'data' , 'data' : vps }
	return template_loader.render('coba.html',data)
	

    @cherrypy.expose
    def list_vps(self):
	nguk = ['bram','huh']
	data = { 'nama' : 'data' , 'data' : nguk }
	return template_loader.render('coba.html',data)
	
