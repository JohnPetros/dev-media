from pytest import raises, fixture

from core.entities import SocialMediaRecord
from core.use_cases import GetDetailsPageData
from core.entities.tests.fakers import SocialMediaRecordsFaker

from core.use_cases.tests.mocks.repositories import (
    SocialMediaRecordRepositoryMock,
)


def describe_get_details_page_data_use_case():
    @fixture
    def repository():
        return SocialMediaRecordRepositoryMock()

    @fixture
    def current_record():
        return SocialMediaRecordsFaker.create(
            github_followers_count="1000",
            twitter_followers_count="1000",
            instagram_followers_count="1000",
            youtube_subscribers_count="1000",
            github_repos_count="30",
            github_stars_count="90",
            instagram_posts_count="150",
            instagram_likes_count="2001",
            twitter_retweets_count="3000",
            twitter_likes_count="5",
            youtube_views_count="Indisponível",
            youtube_videos_count="0",
        )

    @fixture
    def yesterday_record():
        return SocialMediaRecordsFaker.create(
            github_followers_count="500",
            twitter_followers_count="1500",
            instagram_followers_count="500",
            youtube_subscribers_count="1000",
            github_repos_count="15",
            github_stars_count="90",
            instagram_posts_count="0",
            instagram_likes_count="2000",
            twitter_retweets_count="30",
            twitter_likes_count="500",
            youtube_views_count="1750",
            youtube_videos_count="Indisponível",
        )

    @fixture
    def get_details_page_data(
        repository: SocialMediaRecordRepositoryMock,
    ):
        return GetDetailsPageData(
            repository,
        )

    def it_should_throw_exception_if_there_is_no_current_social_media_record(
        get_details_page_data: GetDetailsPageData,
    ):
        with raises(Exception) as exception:
            get_details_page_data.execute(current_social_media_record=None)

        assert str(exception.value) == "Current social media record not found"

    def it_should_return_each_variation_as_zero_if_there_is_no_current_social_media_record_from_yesterday(
        get_details_page_data: GetDetailsPageData,
        current_record: SocialMediaRecord,
        repository: SocialMediaRecordRepositoryMock,
    ):

        repository.get_from_yesterday = lambda _: None

        data = get_details_page_data.execute(current_record)

        absolute_variations_values = [
            variation == "0" for variation in data["absolute_variations"].values()
        ]

        percentage_variations_values = [
            variation == "0" for variation in data["percentage_variations"].values()
        ]

        assert all(absolute_variations_values)
        assert all(percentage_variations_values)

    def it_should_return_absolute_variations(
        get_details_page_data: GetDetailsPageData,
        current_record: SocialMediaRecord,
        yesterday_record: SocialMediaRecord,
        repository: SocialMediaRecordRepositoryMock,
    ):

        repository.get_from_yesterday = lambda _: yesterday_record

        data = get_details_page_data.execute(current_record)

        assert data["absolute_variations"]["github_followers_count"] == "-500"
        assert data["absolute_variations"]["twitter_followers_count"] == "500"
        assert data["absolute_variations"]["instagram_followers_count"] == "-500"
        assert data["absolute_variations"]["youtube_subscribers_count"] == "0"

    def it_should_return_percentage_variations(
        get_details_page_data: GetDetailsPageData,
        current_record: SocialMediaRecord,
        yesterday_record: SocialMediaRecord,
        repository: SocialMediaRecordRepositoryMock,
    ):

        repository.get_from_yesterday = lambda _: yesterday_record

        data = get_details_page_data.execute(current_record)

        assert data["percentage_variations"]["github_repos_count"] == "100.0"
        assert data["percentage_variations"]["github_stars_count"] == "0.0"
        assert data["percentage_variations"]["twitter_retweets_count"] == "9900.0"
        assert data["percentage_variations"]["twitter_likes_count"] == "-99.0"
        assert data["percentage_variations"]["instagram_posts_count"] == "0.0"
        assert data["percentage_variations"]["instagram_likes_count"] == "0.1"
        assert data["percentage_variations"]["youtube_views_count"] == "0.0"
        assert data["percentage_variations"]["youtube_videos_count"] == "0.0"
