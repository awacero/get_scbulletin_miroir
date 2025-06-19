'''
Created on Mar 8, 2023
@author: wacero
'''

import subprocess
from flask import Flask, request, Response, current_app, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from . import main


@main.route('/get_scbulletin')
def call_get_bulletin():

    """
    Allows to call ``scbulletin`` function once access token
    was verified, and then gets the bulletin for an event
    :returns: (text_file)
    :rtype: text
    """

    security_token = generate_password_hash(current_app.config['ACCESS_TOKEN'])
    db_user = current_app.config['DB_USER']
    db_password = current_app.config['DB_PASSWORD']
    db_host = current_app.config['DB_HOST']
    db_name = current_app.config['DB_NAME']

    token = request.args.get('token')
    
    
    if check_password_hash(security_token, token):
        print("Token checked")
        event_id = str(request.args.get('event_id'))
        user = str(request.args.get('user'))
        print("Data received %s %s " %(event_id, user))
        if user=='gv':

            try:
                with open(f"/tmp/{event_id}.txt", "w") as out:
                    subprocess.run(
                        [
                            "seiscomp-python",
                            "/opt/varios/scbulletin_gv.py",
                            "-d",
                            f"mysql://{db_user}:{db_password}@{db_host}/{db_name}",
                            "-x", "-e", "-p", "-3", "-E", event_id
                        ],
                        check=True,
                        stdout=out
                    )
            except Exception as e:
                print(f"Error in scbulletin_gv: {e}")

        elif user=='ms':
            try:
                with open(f"/tmp/{event_id}.txt", "w") as out:
                    subprocess.run(
                        [
                            "seiscomp-python",
                            "/opt/varios/scbulletin_ms.py",
                            "-d",
                            f"mysql://{db_user}:{db_password}@{db_host}/{db_name}",
                            "-x", "-e", "-p", "-3", "-E", event_id
                        ],
                        check=True,
                        stdout=out
                    )
            except Exception as e:
                print(f"Error in scbulletin_ms: {e}")
        
        try:
            return send_from_directory('/tmp/','%s.txt'%event_id,as_attachment=True)
        except FileNotFoundError:
            abort(404)
    else:
        return ("NO token given") 

