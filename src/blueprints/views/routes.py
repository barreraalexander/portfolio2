from flask import Blueprint, render_template, request
from src import cache, schemas, bcrypt
from src.constants import DEFAULT_SETTINGS
from copy import deepcopy

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    default_settings = deepcopy(DEFAULT_SETTINGS)
    requestor_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    if cache.has(request.remote_addr):
        user_settings = cache.get(requestor_ip)
        default_settings.update(user_settings)
    
    # print ('ran')
    return render_template(
        'index.html',
        default_settings=default_settings
    )
