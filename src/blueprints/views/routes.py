from flask import Blueprint, render_template
from src import cache

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
