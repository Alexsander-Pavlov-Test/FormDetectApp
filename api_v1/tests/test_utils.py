import pytest
from api_v1.forms.utils import ConvertObjectIDMixin


class TestUtils:

    @pytest.mark.utils
    def test_converter_key_id(self, dictionary):
        mixin = ConvertObjectIDMixin()
        converted_dict = mixin.convert_id(
            dictionary=dictionary,
        )
        assert converted_dict.get('id') is not None
        assert converted_dict.get('_id') is None
