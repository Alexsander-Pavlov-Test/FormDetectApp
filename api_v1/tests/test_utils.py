import pytest

from api_v1.forms.type_converters import DefaultTypeConverter


class TestUtils:

    @pytest.mark.utils
    def test_convert_dict(self, dictionary_to_convert):
        converter = DefaultTypeConverter(
            target=dictionary_to_convert,
        )
        new_dict = converter.convert()
        assert new_dict == dict(
            name='text',
            phone='phone',
            email='email',
            date1='date',
            date2='date',
            integer='int',
            float_='float',
        )

    @pytest.mark.utils
    def test_pattern_values(self, dictionary_to_convert):
        converter = DefaultTypeConverter(
            target=dictionary_to_convert,
        )
        pattern_dict = converter.get_for_pattern()
        assert pattern_dict == dict(
            name='text',
            phone='phone',
            email='email',
            date1='date',
            date2='date',
        )
