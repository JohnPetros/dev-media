from pytest import raises

from core.structs import Count
from core.errors import ValidationError


def describe_count_struct():
    def it_should_throw_a_exception_if_value_is_not_string():
        with raises(ValidationError) as error:
            Count(42)

        assert str(error.value) == "Count value value must be a string"

    def it_should_format_value_if_it_is_above_or_equal_to_1K():
        assert Count("1000").format().get_value() == "1.0K"
        assert Count("1500").format().get_value() == "1.5K"
        assert Count("20500").format().get_value() == "20.5K"
        assert Count("345010").format().get_value() == "345.0K"

    def it_should_format_value_if_it_is_above_or_equal_to_1M():
        assert Count("1000000").format().get_value() == "1.0M"
        assert Count("1500000").format().get_value() == "1.5M"
        assert Count("1500025").format().get_value() == "1.5M"
        assert Count("12000000").format().get_value() == "12.0M"

    def it_should_not_format_value_if_it_is_not_numeric():
        assert Count("Not available").format().get_value() == "Not available"
