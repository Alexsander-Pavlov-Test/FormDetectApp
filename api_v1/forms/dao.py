from api_v1.forms.mixins import FindPrefechFormMixin
from config.dao import BaseDAO
from config import db_connection


class FormDAO(BaseDAO, FindPrefechFormMixin):
    """
    DAO формы
    """
    model = db_connection.forms
