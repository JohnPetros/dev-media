from os import getenv

from flask import render_template

from infra.factories.use_cases import get_page_data, get_details_page_data

from infra.constants import SOCIAL_MEDIA, INTERNAL_ERROR_MESSAGE

developer_id = int(getenv("DEVELOPER_ID"))


def details_page_view():
    try:
        data = get_page_data.execute(developer_id)

        developer = data["developer"]
        social_media_record = data["social_media_record"]

        details_page_data = get_details_page_data.execute(social_media_record)

        absolute_variations = details_page_data["absolute_variations"]
        percentage_variations = details_page_data["percentage_variations"]

        return render_template(
            "pages/details.html",
            developer=developer,
            social_media_record=social_media_record,
            absolute_variations=absolute_variations,
            percentage_variations=percentage_variations,
            github_logo_color=SOCIAL_MEDIA["github"]["color"],
            twitter_logo_color=SOCIAL_MEDIA["twitter"]["color"],
            instagram_logo_color=SOCIAL_MEDIA["instagram"]["color"],
            youtube_logo_color=SOCIAL_MEDIA["youtube"]["color"],
        )

    except Exception as exception:
        print(f"Details Page View Error: {exception}", flush=True)
        return INTERNAL_ERROR_MESSAGE
