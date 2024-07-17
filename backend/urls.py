#!/usr/bin/python
# -*- coding: UTF-8 -*-

from backend.views import account

# Blueprint Registration
def register(app):
    app.register_blueprint(account, url_prefix='/account', strict_slashes=False)