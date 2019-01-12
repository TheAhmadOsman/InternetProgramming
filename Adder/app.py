from flask import Flask, request, jsonify, Response
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/adder')
def addtwo():
	num1 = int(request.arg['num1'])
	num2 = int(request.args['num2'])
	print("Hello from here!")
	#res = Response(json.dumps(num1+num2))
	#res.headers = {'Content-Type': 'application/json'}
	#return res
	return jsonify(num1+num2)

if __name__ == "__main__":
	#app.run(debug=True, port=5001)
	app.run()
