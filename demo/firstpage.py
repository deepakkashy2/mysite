# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:26:43 2020

@author: deepak
"""


##site
## from libery we need to import Flask 
from flask import Flask,render_template

#need to initiate Flask object
'''
__name__ is just a convenient way to get the import name of the place the app
 is defined. Flask uses the import name to know where to look up resources,
 templates, static files, instance folder, etc. When using a package, 
 if you define your app in __init__.pythen the __name__ will still point at
 the "correct" place relative to where the resources are. However, 
 if you define it elsewhere, such as mypackage/app.py, 
 then using __name__ would tell Flask to look for resources relative 
 to mypackage.app instead of mypackage.
Using __name__ isn't orthogonal to "hardcoding", it's just a shortcut 
to using the name of the package. And there's also no reason to say that 
the name should be the base package, it's entirely up to your project 
structure.
'''
app=Flask(__name__)

#url for theapp
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")
    

if __name__=='__main__':
    app.run(debug=True)