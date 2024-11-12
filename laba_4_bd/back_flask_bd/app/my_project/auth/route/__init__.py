from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.user_route import user_bp
    from .orders.chat_route import chat_bp
    from .orders.chat_participant_route import chat_participant_bp
    from .orders.user_status_route import user_status_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(chat_participant_bp)
    app.register_blueprint(user_status_bp)