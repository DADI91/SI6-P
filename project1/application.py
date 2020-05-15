import os

from flask import *
import sqlite3 as sql
import csv


app = Flask(__name__)
app.secret_key = "cle_secret"


@app.route("index")
def index():
    return "Project 1: TODO"

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
