# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory
from scraper import scrap_atos
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrap', methods=['GET'])
def scrap():
    scrap_atos()
    return send_from_directory('files', 'leis.zip', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
