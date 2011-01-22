import os
import glob
import cherrypy
import hashlib

def hashing(message):
    s = hashlib.sha512()
    s.update(message)
    salt = s.hexdigest()
    l = len(message)
    r = range(l)

    for huruf in r:
		ab = message[huruf]
		s.update(ab)
		p = s.hexdigest()
		pesan = p+salt

    final = hashlib.sha256(pesan).hexdigest()
    return final

def sanitize(message):
    forbiden = ["'",'!','@','#','$','%','^','&','*','(',')','+','=','/','-','|','~',';',':','"','{','}','[',']',',','.']
    for data in forbiden:
      result = message.replace(data,'')
    
    return result
    
def get_setting(item):
	
	return item
