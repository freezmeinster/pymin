from lib import db

def get_setting(setting):
     data = db.query_select("select nilai from setting where nama like '"+setting+"'") 
     return data[0]