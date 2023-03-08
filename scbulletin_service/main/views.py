'''
Created on Mar 8, 2023
@author: wacero
'''

import subprocess 
from flask import Flask, request, Response, current_app, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from . import main


@main.route('/get_bulletin')
def call_get_bulletin():

    """
    Allows to call ``scbulletin`` function once access token
    was verified, and then gets the bulletin for an event
    :returns: (text_file)
    :rtype: text
    """

    security_token = generate_password_hash(current_app.config['ACCESS_TOKEN'])

    token = request.args.get('token')
    
    
    if check_password_hash(security_token, token):
        print("Token checked")
        event_id = str(request.args.get('event_id'))
        user = str(request.args.get('user'))
        print("Data received %s %s " %(event_id, user))
        if user=='gv':
            
            try:
                scbulletin_result = subprocess.call(['''python3 /opt/varios/scbulletin_gv.py -d mysql://sysop:sysop@localhost/seiscomp -x -e -p -3 -E %s > /tmp/%s.txt''' %(event_id,event_id)], shell=True )
                print(scbulletin_result) 
            except Exception as e:
                print("Error in scbulletin_gv: %s %s" %(scbulletin_result,e))
        try:
            return send_from_directory('/tmp/','%s.txt'%event_id,as_attachment=True)
        except FileNotFoundError:
            abort(404)
    else:
        return ("NO token given") 

