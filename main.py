from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return jsonify({'message': 'Hey!'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
