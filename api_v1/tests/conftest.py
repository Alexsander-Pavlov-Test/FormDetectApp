import pytest
from bson.objectid import ObjectId


@pytest.fixture
def dictionary():
    return dict(_id=ObjectId('67543b74156c9dedf8334542'),
                name='some_name',
                value='email',
                value_2='phone',
                )
