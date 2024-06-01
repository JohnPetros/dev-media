from os import getenv

from flask import render_template

from core.use_cases import get_page_data
from infra.constants import SOCIAL_MEDIA, INTERNAL_ERROR_MESSAGE

developer_id = getenv("DEVELOPER_ID")


def home_page_view():
    try:
        data = get_page_data.execute(developer_id)

        developer = data["developer"]
        social_media_record = data["social_media_record"]

        return render_template(
            "pages/home.html",
            developer=developer,
            social_media_record=social_media_record,
            github_logo_color=SOCIAL_MEDIA["github"]["color"],
            github_logo_background_color=SOCIAL_MEDIA["github"]["background_color"],
            twitter_logo_color=SOCIAL_MEDIA["twitter"]["color"],
            twitter_logo_background_color=SOCIAL_MEDIA["twitter"]["background_color"],
            instagram_logo_color=SOCIAL_MEDIA["instagram"]["color"],
            instagram_logo_background_color=SOCIAL_MEDIA["instagram"][
                "background_color"
            ],
            youtube_logo_color=SOCIAL_MEDIA["youtube"]["color"],
            youtube_logo_background_color=SOCIAL_MEDIA["youtube"]["background_color"],
        )

    except Exception as exception:
        print(f"Home Page View Error: {exception}", flush=True)
        return INTERNAL_ERROR_MESSAGE
