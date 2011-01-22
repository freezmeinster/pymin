import os
import glob
import cherrypy
from lib import item

def list_vps():
         vps_dir = item.get_setting('vserver_dir')
         vps = os.listdir(vps_dir)
         vps.remove('.pkg')
         return vps