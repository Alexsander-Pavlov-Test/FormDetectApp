import pytest

from api_v1.forms.type_converters import DefaultTypeConverter, TypeChecker
from api_v1.forms.utils import (construct_key_value_dictionaries)


class TestUtils:

    @pytest.mark.converter
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

    @pytest.mark.converter
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

    @pytest.mark.converter
    def test_check_types(self, converted_dictionary):
        checker = TypeChecker(converted_dictionary)
        not_raised = checker.convert()
        assert not_raised is not None

    @pytest.mark.converter
    def test_convert_phone(self):
        assert DefaultTypeConverter.convert_phone('+7 913 243 1943') == 'phone'

    @pytest.mark.converter
    def test_convert_email(self):
        assert DefaultTypeConverter.convert_email('some@yandex.ru') == 'email'

    @pytest.mark.converter
    def test_convert_text(self):
        assert DefaultTypeConverter.convert_text('some') == 'text'

    @pytest.mark.converter
    def test_convert_date(self):
        assert DefaultTypeConverter.convert_date('1998-07-02') == 'date'
        assert DefaultTypeConverter.convert_date('02.07.1998') == 'date'

    @pytest.mark.converter
    def test_convert_float(self):
        assert DefaultTypeConverter.convert_float('33.3') == 'float'

    @pytest.mark.converter
    def test_convert_int(self):
        assert DefaultTypeConverter.convert_int('33') == 'int'

    @pytest.mark.utils
    def test_key_value_dictionaries(self, converted_dictionary):
        assert (construct_key_value_dictionaries(converted_dictionary) ==
                [
                    dict(name='text'),
                    dict(phone='phone'),
                    dict(email='email'),
                    dict(date1='date'),
                    dict(date2='date'),
                    ]
                )
