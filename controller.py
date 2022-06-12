from flask import Flask, request, jsonify, Response
import json
import db
# from bson.objectid import ObjectId


def get_data():
    try:
        data = list(db.db.collection.find())
        for x in data:
            x["_id"] = str(x["_id"])
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({'error': 'Server Error'}), status=500, mimetype='application/json')


def create_data():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.get_json()
            print(json)
            db.db.collection.insert_one(json)
        return "Data Inserted Successfully"
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({'error': 'Server Error'}),
            status=500,
            mimetype='application/json'
        )
