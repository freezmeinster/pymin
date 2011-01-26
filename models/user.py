import cherrypy
from lib import item,db

def list_user():
    data_user = db.query_select("select * from pengguna",'all')
    return data_user
