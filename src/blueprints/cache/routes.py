from flask import Blueprint, g, render_template
from src import cache

# bp = Blueprint('cache', __name__)






# @bp.route('/clear')
# def clear():
#     if cache.has('value'):
#         cache.delete('value')
#         res = {'status':'successfully deleted'}
#         return jsonify(res), 200
#     else:
#         res = {'status':'nothing to delete'}
#         return jsonify(res), 404
        


    # if cache.has('value'):
    #     x = cache.get('value')
    # else:
    #     x = randrange(1, 100)
    #     cache.set('value', x)

    # # res = {'value': cache.get('value')}
    # # return jsonify(res), 200
