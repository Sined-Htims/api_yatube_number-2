# Проект Yatube API

## Цель работы:

Научится следующему:
1. Подключать *Django REST Framework*. :heavy_check_mark:
2. Подключать токены аутентификации. :heavy_check_mark:
3. Писать сериализаторы. :heavy_check_mark:
4. Описывать вьюсеты. :heavy_check_mark:
5. Ограничивать взаимодействие пользователей с API при помощи разрешений и валидации данных. :heavy_check_mark:
6. Создавать эндпоинты с помощью роутеров. :heavy_check_mark:
7. Подключать пагинацию к API. :heavy_check_mark:
8. Дорабатывать модели БД, для коректного взаимодествися API с ней. :heavy_check_mark:
9. Подключать бэкенды фильтров и поисков к API. :heavy_check_mark:

## Разворачивание проекта.

1. Установить виртуальное окружение.

```bash
python -m venv venv
```

2. Активировать виртуальное окружение.

```bash
. venv/Scripts/activate
```

3. Установить зависиости из requirements.txt.

```bash
pip install -r requirements.txt
```

4. Перейти в директорию с файлом "manage.py".

```bash
cd ./<название_директории>/
```

5. Применить миграции.

```bash
python manage.py migrate
```

6. Создать суперпользователя.

```bash
python manage.py createsuperuser
```

7. Запустить сервер.

```bash
python manage.py runserver
```

8. Получить API Token для аунтефикации.
   <br>**Все API запросы выполнены через приложение **Postman***
   <br>Для получения API Token'а необходимо во вкладке ***Body*** приложения ***Postman*** передать, ***POST-запросом***, значения для ключей ***'username'*** и ***'password'***, созданного суперпользователя, на соотвествующий эндпоинт:

   ```
   http://127.0.0.1:8000/api/v1/jwt/create/
   ```
    ![Example-get-token](https://github.com/Sined-Htims/Image/blob/main/api_yatube/Example-get-token.png)  
    **На изображении указан эндпоинт из предыдущего спринта, но принцип один и тот же.*

<br>

9.  Добавить полученный API Token в Hedears для работы с последующими запросами.
    <br>Для автоматического предоставления токена серверу, необходимо во вкладке ***Headears*** приложения ***Postman***, установить в значение ключа ***Authorization*** полученный токен из пункта 8, добавив перед ним слово ***Bearer***.
    <br>
    <br>
    ![Example-add-token](https://github.com/Sined-Htims/Image/blob/main/api_yatube/Example-add-token.png)
    **На изображении указано слово Token из предыдущего спринта, но принцип один и тот же, только теперь необходимо указать Bearer.*
    </br>
<br>

10.  Наслаждаться :coffee:

**Приведенные команды используются для Bash/OC Windows*
**Это третий спринт из курса "API: интерфейс взаимодействия программ" от Яндекс.Практикум*
