from flask import Flask,jsonify

app = Flask('')
@app.route('/')	
def home():
	return  "I'm alive"

@app.route('/uppercase/<string:parameter>',methods=['GET'])
def uppercase(parameter):
    return jsonify({"{0}".format(parameter):parameter.upper()})

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8080)
