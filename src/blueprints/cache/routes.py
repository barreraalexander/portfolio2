from flask import Blueprint, request, jsonify
from src import cache

bp = Blueprint('cache_api', __name__)

@bp.route('/toggle_color_mode')
def toggle_color_mode():

    requestor_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    if cache.has(requestor_ip):
        user_settings = cache.get(requestor_ip)

        dark_mode_status = user_settings.get('dark_mode')

        user_settings.update(updated)
        cache.set(requestor_ip, user_settings)

    else:
        updated = {'dark_mode':False}
        cache.set(requestor_ip, updated)

    return jsonify({'hi':'hit'})




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
