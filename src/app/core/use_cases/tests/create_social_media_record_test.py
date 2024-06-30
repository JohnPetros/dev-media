from pytest import raises, fixture

from core.use_cases import CreateSocialMediaRecord
from core.entities.tests.fakers import DevelopersFaker, SocialMediaRecordsFaker

from core.use_cases.tests.mocks.repositories import (
    SocialMediaRecordRepositoryMock,
    DevelopersRepositoryMock,
)
from core.use_cases.tests.mocks.providers import SocialMediaApiProviderMock


def describe_create_social_media_record_use_case():
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
    def use_case(
        developers_repository: DevelopersRepositoryMock,
        social_media_records_repository: SocialMediaRecordRepositoryMock,
        social_media_api_provider: SocialMediaApiProviderMock,
    ):
        return CreateSocialMediaRecord(
            developers_repository=developers_repository,
            social_media_records_repository=social_media_records_repository,
            social_media_api=social_media_api_provider,
        )

    def it_should_throw_an_exception_if_any_developer_id_is_not_provided(
        use_case: CreateSocialMediaRecord,
    ):
        with raises(Exception) as exception:
            use_case.execute(developer_id=None)

        assert str(exception.value) == "Developer id is not provided"

    def it_should_throw_exception_if_there_is_no_developer_found(
        use_case: CreateSocialMediaRecord,
    ):
        with raises(Exception) as exception:
            use_case.execute(developer_id=1)

        assert str(exception.value) == "Developer is not found"

    def it_should_add_social_media_record_from_api(
        use_case: CreateSocialMediaRecord,
        developers_repository: DevelopersRepositoryMock,
        social_media_records_repository: SocialMediaRecordRepositoryMock,
    ):
        fake_developer = DevelopersFaker.create()

        developers_repository.add(fake_developer)

        added_record = use_case.execute(fake_developer.id)

        record_from_repository = (
            social_media_records_repository.get_last_by_developer_id(fake_developer.id)
        )

        assert added_record == record_from_repository
