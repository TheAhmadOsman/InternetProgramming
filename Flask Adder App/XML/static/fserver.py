from flask import Flask, Response
import random, json

app = Flask(__name__)

@app.route('/getnum') # when the url /getnum is called, I'm going to call function getnum() below
def getnum(): # can be called anything
	res = Response(json.dumps({'number':random.randrange(100)})) # dump: python equivalent of stringify
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Content-type'] = 'application/json'
	return res

@app.route('/hello')
def hello():
	return "<h1>Hello World</h1>"

app.run(debug=True, port=5001)
# sudo pip install flask