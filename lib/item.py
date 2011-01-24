def get_setting(setting):
     data = {
	    'vserver_dir' : '/home/vserver',
            'vserver_prefix' : '/usr/local'
	    }
     hasil = data.get(setting)
     return hasil