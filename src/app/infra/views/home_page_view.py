from os import getenv

from flask import render_template

from core.use_cases import get_home_page_data
from infra.constants import SOCIAL_MEDIA

developer_id = getenv("DEVELOPER_ID")


def home_page_view():
    data = get_home_page_data.execute(developer_id)

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
        github_logo_color=SOCIAL_MEDIA["github"]["color"],
        github_logo_background_color=SOCIAL_MEDIA["github"]["color"],
        twitter_logo_color=SOCIAL_MEDIA["twitter"]["color"],
        twitter_logo_background_color=SOCIAL_MEDIA["twitter"]["color"],
        instagram_logo_color=SOCIAL_MEDIA["instagram"]["color"],
        instagram_logo_background_color=SOCIAL_MEDIA["instagram"]["color"],
        youtube_logo_color=SOCIAL_MEDIA["youtube"]["color"],
        youtube_logo_background_color=SOCIAL_MEDIA["youtube"]["color"],
    )
