from pytest import raises, fixture

from core.use_cases import GetPageData
from core.entities.tests.fakers import DevelopersFaker

from core.use_cases.tests.mocks.repositories import (
    DevelopersRepositoryMock,
    SocialMediaRecordRepositoryMock,
)
from core.use_cases.tests.mocks.providers import SocialMediaApiProviderMock


def describe_get_page_data_use_case():
    @fixture
    def developers_repository():
        return DevelopersRepositoryMock()

    @fixture
    def social_media_records_repository():
        return SocialMediaRecordRepositoryMock()

    @fixture
    def social_media_api_provider():
        return SocialMediaApiProviderMock()

    @fixture
    def get_page_data(
        developers_repository,
        social_media_records_repository,
        social_media_api_provider,
    ):
        return GetPageData(
            developers_repository=developers_repository,
            social_media_records_repository=social_media_records_repository,
            social_media_api=social_media_api_provider,
        )

    def it_should_throw_exception_if_there_is_no_developer(get_page_data):
        with raises(Exception) as exception:
            get_page_data.execute(developer_id=None)

        assert str(exception.value) == "Developer not found"

    def it_should_return_developer_and_last_social_media_record_from_database_if_any(
        get_page_data, developers_repository
    ):
        fake_developer = DevelopersFaker.create()

        developers_repository.add(fake_developer)

        print(fake_developer)

        # get_page_data.execute(developer_id=1)

        # assert str(exception.value) == "Developer not found"
