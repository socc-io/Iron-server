from __future__ import with_statement
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from Controller import registerController
from Model.database import init_db, db_session
from secret import *

app = Flask(__name__) # Flask Application Object
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost'
app.secret_key = APP_SECRET_KEY;
init_db()

@app.before_request
def csrf_protect() :
	if not debugMode :
		if request.method == "POST" :
			token = session.pop('csrf_token', None)
			if not token or token != request.form.get('csrf_token') :
				abort(403)

@app.before_request
def admin_protect() :
	if (not debugMode) and ('admin' in request.url) :
		if request.args.get('pasw', '') != ADMIN_PASSWORD :
			abort(403)

@app.teardown_request
def shutdown_session(exception=None) :
	db_session.remove()

registerController(app)

if __name__ == '__main__' :
	app.run(debug=debugMode)