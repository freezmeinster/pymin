#!/usr/bin/env python

import cherrypy
import os.path
from controller import Libpymin, Pymin, Root
from lib import template_loader,setting,item




pymin_config = os.path.join(os.path.dirname(__file__), 'pymin.conf')
root = Root()
root.pymin = Pymin.controller()
root.libpymin = Libpymin.controller()

if __name__ == '__main__':
    cherrypy.quickstart(root, config=pymin_config)
else:
    cherrypy.tree.mount(root, config=pymin_config)

