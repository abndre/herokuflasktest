from flask import Flask
from flask import jsonify

import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO'

@app.route('/api')
def teste():
	end = jsonify({'nome':'Andre'})
	return end

@app.route('/vagalumetop/', methods=['GET'])
def vagalumetop15():
    # e.g: http://localhost:5000/vagalume/?artista='mamomas'
    bar = request.args.to_dict()
    artista = bar['artista']
    test = {'artista':artista}
    test = jsonify(test)
    return test

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)