from flask import Flask, jsonify
from flask_caching import Cache
from flask_assets import Environment
from flask_bcrypt import Bcrypt

from src.config import settings
from src.utils.assets import bundles

cache = Cache()
assets = Environment()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    app.config['DEBUG'] = settings.debug

    with app.app_context():
        assets.init_app(app)
        bcrypt.init_app(app)
        cache.init_app(app)

    assets.register(bundles)
    
    @app.route('/healthcheck')
    def healthcheck():
        status = {'status' : 'good'}
        return jsonify(status), 200

    from src.blueprints.views.routes \
        import bp as views_bp
    from src.blueprints.cache.routes \
        import bp as cache_bp

    app.register_blueprint(views_bp)
    app.register_blueprint(cache_bp)

    return app