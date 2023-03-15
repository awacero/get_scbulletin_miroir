#!/usr/bin/python3
import sys,os
os.environ['FLASK_CONFIG'] = 'production'
os.environ['SEISCOMP_ROOT'] = "/home/seiscomp/seiscomp/"
os.environ['HOME'] = "/home/seiscomp/"

os.environ['PATH'] = f"{os.environ['PATH']}:/home/seiscomp/seiscomp/bin"
os.environ['PYTHONPATH']=f"{os.environ['PATH']}:/home/seiscomp/seiscomp/lib/python:/home/seiscomp/.local/lib/python3.8/"

os.environ['LD_LIBRARY_PATH']= "/home/seiscomp/seiscomp/lib/"
sys.path.insert(0,'/home/seiscomp/seiscomp/lib/python')
sys.path.insert(1,'/home/seiscomp/seiscomp/lib/python/seiscomp3')
sys.path.insert(2,'/home/seiscomp/seiscomp/lib/python/eqelib')
sys.path.insert(3,'/home/seiscomp/.local/lib/python3.8/site-packages')
sys.path.insert(4,'/home/seiscomp/proyectos_codigo/get_scbulletin')

from scbulletin_service import create_app

application = create_app(os.getenv('FLASK_CONFIG') or 'default')
