### Описание
Проект содержит 2 демонстрационных приложения и приложение auto_api для реализации API. В миграции добавлены дата-миграции с данными для демонстрации.

### Установка
- git clone https://github.com/surferslon/rp_test.git
- python3 -m venv rp_test_env
- . ./rp_test_env/bin/activate
- cd rp_test
- pip install -r requirements
- python manage.py migrate
- python manage.py runserver

### Список всех моделей
- Метод: get 
- Адрес: api/rest/v1/auto_api/list

### Поиск в модели
- Метод: get
- Адрес: api/rest/v1/auto_api/search/<имя пирложения>/<имя модели>
- Параметры
    - search={<поле_модели>: <строка_поиска>}  
    - order_by=<поле_модели>
    - limit=<число>

### Создание объекта
- Метод: post
- Адрес: api/rest/v1/create
- Параметры: 
 ```javascript
  {
    "app_name": <имя_приложения>,
    "model_name>": <имя_модели>,
    "fields_data": <данные полей вида {"Имя_поля": "Значение_поля", ...}>
  }
  ```
 
 ### Обновление объекта
 - Метод: put 
 - Адрес: api/rest1/v1/create
 - Параметры:
 ```javascript
  {
    "app_name": <имя_приложения>,
    "model_name>": <имя_модели>,
    "pk": <ключ>,
    "fields_data": <данные полей вида {"имя_поля": "значение_поля", ...}>
  }
 ```
 
 ### Удаление объекта
 - Метод: delete 
 - Адрес: api/rest/v1/delete/<имя пирложения>/<имя модели>/<ключ_объекта>'
 
 ### Тестирование
 python manage.py test auto_api
