from flask import Blueprint

main = Blueprint('main', __name__)

"""
Blueprint for the main application module.

This blueprint defines routes, views, and forms related to the main application module.
"""

from . import views, errors, forms

"""
Importing views, errors, and forms modules.

These modules contain the view functions, error handlers, and forms related to the main application module.
"""
