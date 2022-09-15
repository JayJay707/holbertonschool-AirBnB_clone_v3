#!/usr/bin/python3
"""Index"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API """
    ok_status = {"status": "OK"}
    return jsonify(ok_status)

@app_views.route('/stats')
def stats():
    """
        return dict count of data
    """
    my_dict = {"amenities": storage.count(Amenity),
               "cities": storage.count(City),
               "places": storage.count(Place),
               "reviews": storage.count(Review),
               "states": storage.count(State),
               "users": storage.count(User)}
    return jsonify(my_dict)
