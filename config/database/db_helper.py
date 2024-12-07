from motor import motor_asyncio

from config import settings


DATA_BASE_URL = settings.db.url


class DataBaseHelper:
    """
    Вспомогательный класс для работы с Базой Данных.

    Помогает инициализировать соединение с Базой Данных, а так же
    c таблицами.

    ## Инициализация:
        :string:`db_url` - Адресс базы данных.

    ## Методы:

    ## Примеры:
    ```
    """
    def __init__(self,
                 db_url: str = DATA_BASE_URL,
                 ) -> None:
        """
        Args:
            db_url (str, optional): Адресс Базы Данных. Defaults to DATA_BASE_URL.
        """
        self.client = motor_asyncio.AsyncIOMotorClient(db_url)
        self.database = self.client.forms
        self._forms_collection = (self.database
                                  .get_collection('forms_collection'))

    @property
    def forms(self) -> motor_asyncio.AsyncIOMotorCollection:
        return self._forms_collection


db_helper = DataBaseHelper()
