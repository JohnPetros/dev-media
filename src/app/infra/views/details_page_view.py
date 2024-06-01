from os import getenv

from flask import render_template

from core.use_cases import get_details_page_data
from infra.constants import SOCIAL_MEDIA


developer_id = getenv("DEVELOPER_ID")


def details_page_view():
    data = get_details_page_data.execute(developer_id)

    developer = data["developer"]

    github_followers_count = data["github_followers_count"]
    github_repos_count = data["github_repos_count"]
    github_stars_count = data["github_stars_count"]

    twitter_followers_count = data["twitter_followers_count"]
    twitter_likes_count = data["twitter_likes_count"]
    twitter_retweets_count = data["twitter_retweets_count"]

    instagram_followers_count = data["instagram_followers_count"]
    instagram_posts_count = data["instagram_posts_count"]
    instagram_likes_count = data["instagram_likes_count"]

    youtube_followers_count = data["youtube_followers_count"]

    return render_template(
        "pages/details.html",
        developer=developer,
        github_followers_count=github_followers_count,
        github_repos_count=github_repos_count,
        github_stars_count=github_stars_count,
        twitter_followers_count=twitter_followers_count,
        twitter_likes_count=twitter_likes_count,
        twitter_retweets_count=twitter_retweets_count,
        instagram_followers_count=instagram_followers_count,
        instagram_posts_count=instagram_posts_count,
        instagram_likes_count=instagram_likes_count,
        youtube_followers_count=youtube_followers_count,
        github_logo_color=SOCIAL_MEDIA["github"]["color"],
        twitter_logo_color=SOCIAL_MEDIA["twitter"]["color"],
        instagram_logo_color=SOCIAL_MEDIA["instagram"]["color"],
        youtube_logo_color=SOCIAL_MEDIA["youtube"]["color"],
    )
