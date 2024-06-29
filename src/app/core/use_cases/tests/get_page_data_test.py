from pytest import raises, fixture

from core.use_cases import GetPageData
from core.entities.tests.fakers import DevelopersFaker, SocialMediaRecordsFaker

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

    def it_should_throw_exception_if_there_is_no_developer(get_page_data: GetPageData):
        with raises(Exception) as exception:
            get_page_data.execute(developer_id=None)

        assert str(exception.value) == "Developer not found"

    def it_should_return_developer_and_last_social_media_record_from_database_if_any(
        get_page_data: GetPageData,
        social_media_records_repository: SocialMediaRecordRepositoryMock,
        developers_repository: DevelopersRepositoryMock,
    ):
        fake_developer = DevelopersFaker.create()
        fake_social_media_record = SocialMediaRecordsFaker.create()

        fake_social_media_record.developer = fake_developer

        developers_repository.add(fake_developer)
        social_media_records_repository.add(fake_social_media_record)

        data = get_page_data.execute(developer_id=fake_developer.id)

        assert data["developer"] == fake_developer
        assert data["social_media_record"] == fake_social_media_record

    def it_should_add_a_social_media_record_from_api_if_any_social_media_record_is_found_from_repository(
        get_page_data: GetPageData,
        social_media_records_repository: SocialMediaRecordRepositoryMock,
        developers_repository: DevelopersRepositoryMock,
    ):
        fake_developer = DevelopersFaker.create()

        developers_repository.add(fake_developer)

        data = get_page_data.execute(developer_id=fake_developer.id)

        added_fake_social_media_record = (
            social_media_records_repository.get_last_by_developer_id(fake_developer.id)
        )

        assert data["social_media_record"] == added_fake_social_media_record
        assert data["developer"] == fake_developer
