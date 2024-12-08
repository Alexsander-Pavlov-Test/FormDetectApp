# Title
Приложение для определения заполенных форм.

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
Работать с энд поинтами можно по адруссу http://localhost:8080/docs
## Create
Для создания шаблона найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/create
## Delete
Для удаления шаблонов найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/delete/{id}
## get-form
Для поиска шаблна найдите енд поинт по адрессу http://localhost:8080/api/v1/forms/get_form

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