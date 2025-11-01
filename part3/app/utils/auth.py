"""
Authentication and authorization utilities.
"""
from flask_jwt_extended import get_jwt
from functools import wraps
from flask_restx import abort


def admin_required():
    """
    Decorator to check if the current user is an admin.
    Must be used after @jwt_required().
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if not claims.get('is_admin', False):
                abort(403, 'Admin privileges required')
            return f(*args, **kwargs)
        return wrapper
    return decorator


def is_admin():
    """
    Check if the current authenticated user is an admin.
    Returns True if admin, False otherwise.
    """
    claims = get_jwt()
    return claims.get('is_admin', False)
