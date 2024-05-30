from os import getenv

from flask import Flask, Blueprint, render_template

from controllers import get_developer_by_id_controller

views = Blueprint("view", __name__)

developer_id = getenv("DEVELOPER_ID")


@views.route("/")
def home():
    developer = get_developer_by_id_controller.execute(1)
    return render_template("pages/home.html", developer=developer)


@views.route("/details")
def details():
    return render_template("pages/details.html")


def init_views(app: Flask):
    app.register_blueprint(views)
