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
	     f = open(""+conf_dir+""+a+"/context")
	     fd = f.read()
	     f.close()
	     
	     m = open(""+conf_dir+""+a+"/rlimits/rss.hard")
	     mr = m.read()
	     mn = int(mr)/250
	     m.close()
	     
	     ip = open(""+conf_dir+""+a+"/interfaces/0/ip")
	     ipn = ip.read()
	     ip.close()
	     
	     data += [{'nama_vps' : a.title(),'id' : fd ,'memori' : str(mn) ,'ip' : ipn},]
         return data