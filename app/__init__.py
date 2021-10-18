from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    return app
