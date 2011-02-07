import os
import glob
import cherrypy
from lib import item

def list_vps():
         data = []
         vps_dir = item.get_setting('vserver_dir')
         pref = item.get_setting('vserver_prefix')
         conf_dir = pref+'/etc/vservers/'
         
         vps = os.listdir(vps_dir)
         vps.remove('.pkg')
         
         for a in vps:
	   
	     life = os.popen("sudo "+pref+"/sbin/vserver-stat | grep "+a+"").read()
	     if life != '':
		button = "<input class=\"btnred\" type=\"button\" id=\"\" value=\"Matikan\">"
		f = open(""+conf_dir+""+a+"/context")
		fd = f.read()
		f.close()
	     
		m = open(""+conf_dir+""+a+"/rlimits/rss.hard")
		mu = os.popen("sudo "+pref+"/sbin/vserver-stat | grep "+a+" | awk '{ print $4 }'|cut -d'.' -f1").read()
		mr = m.read()
		ma = (int(mr)/250)-(int(mu))
		mn = int(mr)/250
		m.close()
	       
	     else :
		button = "<input class=\"btn\" type=\"button\" id=\"\" value=\"Hidupkan\">"
		m = open(""+conf_dir+""+a+"/rlimits/rss.hard")
		mr = m.read()
		mn = int(mr)/250
		ma = 0
		f = open(""+conf_dir+""+a+"/context")
		fd = f.read()
		f.close()
	    
	     
	     ip = open(""+conf_dir+""+a+"/interfaces/0/ip")
	     ipn = ip.read()
	     ip.close()
	     
	     
	     
	     
	     data += [{'nama_vps' : a.title(),'id' : fd ,'memori' : str(mn) , 'freemem': str(ma) ,'ip' : ipn, 'button' : button },]
         return data