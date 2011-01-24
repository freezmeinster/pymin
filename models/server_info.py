import os
import glob
import cherrypy
import math
from lib import item

def info():
    data = {}
    #versi kernel 
    k = os.popen("uname -r").read()
    
    #memori total 
    m = os.popen('free | grep Mem | awk \'{print $2}\'')
    mem = int(m.read())/1000
    
    #free memori
    f = os.popen('free | grep Mem | awk \'{print $4}\'')
    fmem = int(f.read())/1000
    persen = int(math.ceil(fmem*100/mem))
    
    #buat warna bar nya
    bar = ''
    if persen <= 40:
	bar = 'highbar'
    elif persen > 40 and persen <= 60  :
	bar = 'midbar'
    elif persen > 60:
	bar = 'lowbar'
    
    #uptime nya
    try:
	f = open( "/proc/uptime" )
	contents = f.read().split()
	f.close()
    except:
	return "Cannot open uptime file: /proc/uptime"

    total_seconds = float(contents[0])
    MINUTE  = 60
    HOUR    = MINUTE * 60
    DAY     = HOUR * 24
    days    = int( total_seconds / DAY )
    hours   = int( ( total_seconds % DAY ) / HOUR )
    minutes = int( ( total_seconds % HOUR ) / MINUTE )
    seconds = int( total_seconds % MINUTE )
    string = ""
    if days> 0:
	string += str(days) + " hari, "
    if len(string)> 0 or hours> 0:
	string += str(hours) + " jam, "
    if len(string)> 0 or minutes> 0:
	string += str(minutes) + " menit, "
	string += str(seconds) + " detik " 
    
    #Cpu load dalam %
    p = os.popen('vmstat | grep 0 | awk \'{ print $13}\'')
    proc = math.ceil(int(p.read()))+1
    procbar = ''
    
    #buat warna bar load cpu 
    if int(proc) <= 30:
	procbar = 'lowbar'
    elif int(proc) > 30 and int(proc) <= 70:
	procbar = 'midbar'
    elif int(proc) > 70:
	procbar = 'highbar'
	
    # cari tahu jenis CPU nya
    jproc = ''
    jp = os.popen("cat /proc/cpuinfo | grep  -m 1 'model name'").read().split()
    for a in jp[3:]:
	jproc += a+' '
    
    data = {
	'memori' 	: str(mem).replace('\n','')+' MB' ,
	'freememori' 	: str(persen).replace('\n',''),
	'freebar' 	: bar,
	'proc' 		: str(proc).replace('\n',''),
	'procbar' 	: procbar,
	'uptime' 	: string,
	'jenis_proc'	: jproc,
	'vkernel'	: str(k)
	}
	
    return data
    
    
def info_vserver():
    data = {}
    vprefix = item.get_setting('vserver_prefix').strip()
    vd = item.get_setting('vserver_dir').strip()
    conf = os.popen(""+vprefix+"/sbin/vserver-info . SYSINFO | grep -m 1 cfg | cut -d':' -f2 | cut -d '}' -f 2").read()
    
    vdevice = os.popen("stat "+vd+" | grep Device | awk '{ print $2}' | cut -d'/' -f1").read()
    mj = vdevice[0:2]
    mn = vdevice[2]
    rd = ''
    if mj == '80':
      rd = '/dev/sda'
    elif mj == '30':
      rd = '/dev/hda'
    
    vf = os.popen("df | grep "+rd+mn+" | awk '{ print $4}'").read()
    vt = os.popen("df | grep "+rd+mn+" | awk '{ print $2}'").read()
    
    byte = 1000000
    suf = ''
    suft = ''
    
    if int(vt)/byte == 0:
      suft = 'Mb'
      hasilt = int(vt)/1000
    elif int(vt)/byte > 0:
      suft = 'Gb'
      hasilt = int(vt)/byte
    
    if int(vf)/byte == 0:
      suf = 'Mb'
      hasil = int(vf)/1000
    elif int(vf)/byte > 0:
      suf = 'Gb'
      hasil = int(vf)/byte
      
    persenmount = hasil*100/hasilt
    if int(hasil) <= 30:
	mountbar = 'highbar'
    elif int(hasil) > 30 and int(hasil) <= 70:
	mountbar = 'midbar'
    elif int(hasil) > 70:
	mountbar = 'lowbar' 
    
      
    data = {
	    'rootdir' 		: vd,
	    'prefix'		: vprefix,
	    'confdir' 		: vprefix+conf,
	    'mount'		: rd+mn ,
	    'totalmount'	: str(hasilt)+suft,
	    'persenmount'	: str(persenmount),
	    'mountbar'		: mountbar
	}
    return data