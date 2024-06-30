from core.entities import SocialMediaRecord
from core.constants import DEFAULT_COUNT_VALUE, VARIATIONS
from core.interfaces.repositories import SocialMediaRecordsRepositoryInterface


class GetDetailsPageData:
    def __init__(
        self, social_media_records_repository: SocialMediaRecordsRepositoryInterface
    ) -> None:
        self.social_media_records_repository = social_media_records_repository

    def execute(self, current_social_media_record: SocialMediaRecord):
        if not isinstance(current_social_media_record, SocialMediaRecord):
            raise Exception("Current social media record not found")

        yesterday_social_media_record = (
            self.social_media_records_repository.get_from_yesterday(
                current_social_media_record
            )
        )

        absolute_variation_attributes = VARIATIONS["absolute_variation_attributes"]
        percentage_variation_attributes = VARIATIONS["percentage_variation_attributes"]

        absolute_variations = {
            attribute: "0" for attribute in absolute_variation_attributes
        }

        percentage_variations = {
            attribute: "0" for attribute in percentage_variation_attributes
        }

        if not isinstance(yesterday_social_media_record, SocialMediaRecord):
            return {
                "absolute_variations": absolute_variations,
                "percentage_variations": percentage_variations,
            }

        for attribute in percentage_variation_attributes:
            percentage_variations[attribute] = self.__get_variation(
                current_social_media_record=current_social_media_record,
                yesterday_social_media_record=yesterday_social_media_record,
                attribute=attribute,
                is_percentage=True,
            )

        for attribute in absolute_variation_attributes:
            absolute_variations[attribute] = self.__get_variation(
                current_social_media_record=current_social_media_record,
                yesterday_social_media_record=yesterday_social_media_record,
                attribute=attribute,
                is_percentage=False,
            )

        return {
            "absolute_variations": absolute_variations,
            "percentage_variations": percentage_variations,
        }

    def __get_variation(
        self,
        current_social_media_record: SocialMediaRecord,
        yesterday_social_media_record: SocialMediaRecord,
        attribute: str,
        is_percentage: bool,
    ):
        current_value = getattr(current_social_media_record, attribute).get_value()
        yesterday_value = getattr(yesterday_social_media_record, attribute).get_value()

        if (
            current_value == DEFAULT_COUNT_VALUE
            or yesterday_value == DEFAULT_COUNT_VALUE
        ):
            return "0.0"

        difference = int(yesterday_value) - int(current_value)

        if is_percentage:
            if int(yesterday_value) == 0:
                return "0.0"

            percentage = -difference / int(yesterday_value) * 100
            return f"{percentage:0.1f}"

        return str(difference)
