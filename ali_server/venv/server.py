from flask import Flask
from flask import request, json
import sqlite3

app = Flask(__name__)
# db_conn = sqlite3.connect('ali_master.db')

# TODO:
"""
- basic auth (uname, password) --> api key (hash this when sending it over)
- storage (sqlite3) --> lots of reads, not a lot of writes 
- rate limiting (requests from same ip/key, file size limit)

"""

# @app.route('/shalom')
# def shalom():
#     return 'shalom'

# will take secure hash from ali cli: uname + pass
# add to db
# return result (success or error)
@app.route('/register/', methods=['POST'])
def register():
	print(request.json)
	# print(request)
	return request.json
   
# # read from local download folder, push  
# @app.route('/upload/<string:khash>&<string:fname>&<string:pname>', methods=['POST'])
# def upload_plugin():
# 	pass

# # read from db/file_store... return 
# @app.route('/upload/<string:khash>&<string:pname>', methods=['GET'])
# def download_plugin():
# 	pass






