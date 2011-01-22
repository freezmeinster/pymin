def get_setting(setting):
     data = {
	    'vserver_dir' : '/home/vserver/',
            'vserver_conf' : '/usr/local/etc/vservers/'
	    }
     hasil = data.get(setting)
     return hasil