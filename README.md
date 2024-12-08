# Title
Приложение для определения заполенных форм.
Это очень удобное приложение которое может автоматически Определить
форму подходящую под запрос, либо сгенерировать новую.
# View
## Конверторы типов.
Конверторы типов играют важную роль,
они обеспечивают нужный тип данных для дальнейшей обработки
на протяжении всей работы программы.
- BaseTypeConverter
- DefaultTypeConverter
- TypeChecker

BaseTypeConverter -
Базовый конвертор предназначен только для наследования,
реализует базовый функционал.

DefaultTypeConverter -
"Дэфолтный" конвертор который стандартным образом
обеспечивает конвертацию данных. В данном контексте
конвертация происходит по опозданию типа данных.
Опознаный тип выводится.

```python
from config import settings
from api_v1.forms.type_converters import DefaultTypeConverter


values = dict(
    phone='+74304324243',
    email='some@yandex.ru',
    date='2024-01-01',
    text='some_text',
    integer='33',
    float_='44.3',
)
converter = DefaultTypeConverter(value=values)
# Получение словаря с конвертированными значениями
converter.convert()
<<
{
    phone: 'phone',
    email: 'email',
    date: 'date',
    text: 'text',
    integer: 'integer',
    float_: 'float',
}
>>
# Получение словаря только с декларированными полями
converter.get_for_pattern()
<<
{
    phone: 'phone',
    email: 'email',
    date: 'date',
    text: 'text',
}
>>
```

TypeChecker -
Конвертор который проверяет что значение ключа является
стандатом декларированного протокола.

```python
from config import settings
from api_v1.forms.type_converters import TypeChecker


values = dict(
    phone='phone',
    email='email',
    date='date',
    text='text',
)
converter = TypeChecker(value=values)
# Данный метод проходится по значением и проводит проверку
converter.convert()
```
# Quick start
## Enviroments
Необходимо заполнить **.env.sample** и в последствии перемеиновать его в **.env**
```python
# .env.sample
MONGO_PASSWORD=password # Пароль от базы данных (Настройка)
```
## Docker
Шаблон находится под системой управления и контеризации - **Docker**.
Если у вас нет Docker - вы можете установить его с официального сайта: [Docker](https://www.docker.com/get-started/)
- Вам необходимо сделать "Билд"
```bash
docker compose build
```
- Вам необходимо запустить окружение
```bash
docker compose up
```
- После успешного запуска приложение будет доступно по адрессу: http://localhost:8080
# Usage
Работать с энд поинтами можно по адрeссу http://localhost:8080/docs
## Create
Для создания шаблона найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/create
## Delete
Для удаления шаблонов найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/delete/{id}
## get-form
Для поиска шаблона найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/get_form

# Test
Для того что бы провести тесты нужно зайти в docker image и провести там тесты:
```bash
docker ps
```
Найдите ID контейнера который вмещает в себя приложение
```bash
docker exec -it ID bash
```
- Для запуска используйте команду
```bash
pytest
```
Будут проведены тесты.