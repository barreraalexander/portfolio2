from flask import Blueprint, render_template

router = Blueprint(
    'main',
    __name__
)

@router.route('/')
def index():
    return render_template(
        'index.html',
    )