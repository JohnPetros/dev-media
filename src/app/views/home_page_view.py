from os import getenv

from flask import render_template

from controllers import home_page_controller

developer_id = getenv("DEVELOPER_ID")


def home_page_view():
    data = home_page_controller.execute(developer_id)

    developer = data["developer"]

    github_followers_count = data["github_followers_count"]
    github_link = data["github_link"]

    twitter_link = data["twitter_link"]
    twitter_followers_count = data["twitter_followers_count"]

    instagram_link = data["instagram_link"]
    instagram_followers_count = data["instagram_followers_count"]

    youtube_link = data["youtube_link"]
    youtube_followers_count = data["youtube_followers_count"]

    return render_template(
        "pages/home.html",
        developer=developer,
        github_followers_count=github_followers_count,
        github_link=github_link,
        twitter_followers_count=twitter_followers_count,
        twitter_link=twitter_link,
        instagram_link=instagram_link,
        instagram_followers_count=instagram_followers_count,
        youtube_link=youtube_link,
        youtube_followers_count=youtube_followers_count,
    )
