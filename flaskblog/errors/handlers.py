"""TODO:Add module docstring"""

from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(unused_error):
    """Handles 404 Not Found errors"""
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(unused_error):
    """TODO: Handles 403 Forbidden errors"""
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(unused_error):
    """TODO: Handles 500 Server errors"""
    return render_template('errors/500.html'), 500
