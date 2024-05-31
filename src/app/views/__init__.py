from flask import Flask, Blueprint

from .home_page_view import home_page_view
from .details_page_view import details_page_view

views = Blueprint("view", __name__)

views.add_url_rule("/", view_func=home_page_view)
views.add_url_rule("/details", view_func=details_page_view)


def init_views(app: Flask):
    app.register_blueprint(views)
