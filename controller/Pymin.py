import cherrypy,os
from lib import template_loader,setting,item
from models import *

class controller():
    
    @cherrypy.expose
    def index(self):
        vps = vps_info.list_vps()
	data = {'url' : '/pymin','head' : 'Sistem', 'branch' : 'List Vserver','nama' : 'Vserver yang telah terdaftar pada sistem Pymin' , 'data' : vps }
	return template_loader.render('list_vps.html',data)
	
    @cherrypy.expose
    def buat_vps(self):
	vps = vps_info.list_vps()
	data = {'url' : '/pymin/buat_vps', 'head' : 'Sistem', 'branch' : 'Buat Vserver', 'nama' : 'Buat Vserver baru' , 'data' : vps }
	return template_loader.render('buat_vps.html',data)
	
    
    @cherrypy.expose
    def vps_berjalan(self):
	vps = vps_info.list_vps()
	data = {'url' : '/pymin/vps_berjalan', 'head' : 'Sistem' , 'branch' : 'Vserver Berjalan', 'nama' : 'Vserver yang sedang berjalan pada sistem Pymin' , 'data' : vps }
	return template_loader.render('buat_vps.html',data)