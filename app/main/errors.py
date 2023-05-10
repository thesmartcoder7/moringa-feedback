from flask import render_template
from . import main

# 404 page 
@main.app_errorhandler(404)
def notfound(error):
    return render_template('notfound.html'), 404