#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
# http://10.103.241.91:10101/account/return_json
from flask import Blueprint, jsonify, app, request
# from .reactt import*
import numpy as np
import matplotlib.pyplot as plt
from .all_test import*
from flask_cors import *
from backend import func_show


    #   
account = Blueprint('/account', __name__)
CORS(account, supports_credentials=True)


    # Visit the link http://host:port/account/return_json and you will be redirected here
@account.route('/post_json', methods=['POST'])
# @cross_origin()
    # The link above is bound to this method. We request a json format return to the browser or interface
    #http://127.0.0.1:10101/account/post_json
    # http://10.103.241.91/account/return_json

def post_json():
    if request.method == 'POST':
        request_data = request.get_data().decode('utf-8')
        # Encode before parsing json. Otherwise the result will not be in Chinese
        
        func_show.file(all_run(json.loads(request_data)))
        # return 'post_json'
    return 'post_json'

@account.route('/return_json')
# @cross_origin()
def return_json():
    path = "./data/output.json"
    with open(path, "r", encoding="utf-8") as f:
        load_dict = json.load(f)
        # print(load_dict)
    # return jsonify(load_dict)
    return jsonify({'code': 0, 'content': 'hi flask'})

