from flask import Blueprint, g, jsonify
from random import randrange
from src import cache
bp = Blueprint('views', __name__)

@bp.route('/')
def index():

    if cache.has('value'):
        x = cache.get('value')
    else:
        x = randrange(1, 100)
        cache.set('value', x)

    res = {'value': cache.get('value')}
    return jsonify(res), 200


@bp.route('/clear')
def clear():
    if cache.has('value'):
        cache.delete('value')
        res = {'status':'successfully deleted'}
        return jsonify(res), 200
    else:
        res = {'status':'nothing to delete'}
        return jsonify(res), 404
        

