"""
Error Handling Module

This module defines error handling for the main application module.
It handles HTTP 404 errors and renders a custom 'notfound.html' template.

Functions:
    notfound(error): Handles HTTP 404 errors and renders the 'notfound.html' template.

Usage Example:
    from flask import Flask
    from . import main, errors

    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(errors)

"""

from flask import render_template
from . import main

@main.app_errorhandler(404)
def notfound(error):
    """
    Handle HTTP 404 (Not Found) errors and render the 'notfound.html' template.

    Args:
        error (Exception): The exception representing the 404 error.

    Returns:
        tuple: A tuple containing the response and the HTTP status code (404).
               The response is the rendered 'notfound.html' template.

    Example:
        When a route is not found, Flask will raise a 404 error and trigger this function
        to render the 'notfound.html' template and return it along with the HTTP status code 404.

    """
    return render_template('notfound.html'), 404
