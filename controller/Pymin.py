import cherrypy,os
from lib import template_loader,setting,item
from models import vps_info,server_info,user

class controller():
    
    @cherrypy.expose
    def index(self):
        vps = vps_info.list_vps()
	data = {'url' : '/pymin','head' : 'Pengaturan Vserver', 'branch' : 'List Vserver','nama' : 'Vserver yang telah terdaftar pada sistem Pymin' , 'data' : vps }
	return template_loader.render('list_vps.html',data)
	
    @cherrypy.expose
    def buat_vps(self):
	vps = vps_info.list_vps()
	data = {'url' : '/pymin/buat_vps', 'head' : 'Pengaturan Vserver', 'branch' : 'Buat Vserver', 'nama' : 'Buat Vserver baru' , 'data' : vps }
	return template_loader.render('buat_vps.html',data)
	
    
    @cherrypy.expose
    def vps_berjalan(self):
	vps = vps_info.list_vps()
	data = {'url' : '/pymin/vps_berjalan', 'head' : 'Pengaturan Vserver' , 'branch' : 'Vserver Berjalan', 'nama' : 'Vserver yang sedang berjalan pada sistem Pymin' , 'data' : vps }
	return template_loader.render('vps_berjalan.html',data)
	

    @cherrypy.expose
    def status_server(self):
	status = server_info.info()
	vserver = server_info.info_vserver()
	data = {'url' : '/pymin/tentang', 'head' : 'Pengaturan Sistem' , 'branch' : 'Status Server', 'nama' : 'Informasi Mengenai Server ', 'data' : status,'vserver': vserver}
	return template_loader.render('status.html',data)
	
    @cherrypy.expose
    def log(self):
	data = {'url' : '/pymin/tentang', 'head' : 'Pengaturan Sistem' , 'branch' : 'Catatan Sistem', 'nama' : 'Catatan sistem Pymin' }
	return template_loader.render('log.html',data)
	
    @cherrypy.expose
    def tentang(self):
	
	data = {'url' : '/pymin/tentang', 'head' : 'Pengaturan Sistem' , 'branch' : 'Tentang Pymin', 'nama' : 'Informasi singkat tentang Pymin' }
	return template_loader.render('tentang.html',data)
	
    @cherrypy.expose
    def pengguna(self):
	data_user = user.list_user()
	data = {'url' : '/pymin/pengguna', 'head' : 'Pengaturan Sistem' , 'branch' : 'Pengguna Pymin', 'nama' : 'Pengaturan Pengguna Pymin','data': data_user, }
	return template_loader.render('pengguna.html',data)
	

    @cherrypy.expose
    def sistem(self):
	data = {'url' : '/pymin/sistem', 'head' : 'Pengaturan Sistem' , 'branch' : 'Sistem Pymin', 'nama' : 'Pengaturan Sistem Pymin' }
	return template_loader.render('sistem.html',data)