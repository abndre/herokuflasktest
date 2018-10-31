from flask import Flask, request
from flask import jsonify

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

options = ChromeOptions()
options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
driver = webdriver.Chrome(chrome_options=options)


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
    # e.g: http://localhost:5000/vagalumetop/?artista='mamomas'
    bar = request.args.to_dict()
    artista = bar['artista']
    test = {'artista':artista}
    test = jsonify(test)
    return test

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

#heroku buildpacks:add https://github.com/kevinsawicki/heroku-buildpack-xvfb-google-chrome/ --app
#heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver --app
#heroku stack:set cedar-14 -a stocksdata --app
