from flask import Flask

from views import init_views
from database import init_database


def init_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    init_views(app)
    init_database()

    return app
