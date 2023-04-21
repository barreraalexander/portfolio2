from flask import Blueprint, render_template, request
from src import cache, schemas, bcrypt
from src.constants import DEFAULT_SETTINGS
from copy import deepcopy

bp = Blueprint('views', __name__)

@bp.route('/')
# @cache.cached(timeout=300)
def index():
    return render_template(
        'index.html',
    )
