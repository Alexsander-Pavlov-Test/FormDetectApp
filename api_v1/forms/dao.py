from config.dao import BaseDAO
from config import db_connection


class FormDAO(BaseDAO):
    """
    DAO формы
    """
    model = db_connection.forms
