#!/usr/bin/python3
"""
application view
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """return status OK"""
    resp = {
        'status': "OK"
    }
    return jsonify(resp)
