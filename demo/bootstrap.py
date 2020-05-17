# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:26:43 2020

@author: deepak
"""


##site
## from libery we need to import Flask 
from flask import Flask,render_template

#need to initiate Flask object
app=Flask(__name__)

#url for theapp
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/sam/')
def sam():
    return render_template("sam.html")
    

if __name__=='__main__':
    app.run(debug=True)