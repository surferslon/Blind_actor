### Description
The project contains 2 demo applications and an auto_api application to implement the API. Added data migrations to migrations with demo data.

### Installation
- git clone https://github.com/surferslon/rp_test.git
- python3 -m venv rp_test_env
- . ./rp_test_env/bin/activate
-cd rp_test
- pip install -r requirements
- python manage.py migrate
- python manage.py runserver

### List of all models
- Method: get
- Address: api/rest/v1/auto_api/list

### Search in the model
- Method: get
- Address: api/rest/v1/auto_api/search/<application name>/<model name>
- Options
    - search={<model_field>: <search_string>}
    - order_by=<model_field>
    -limit=<number>

### Create an object
- Method: post
- Address: api/rest/v1/create
- Options:
 ```javascript
  {
    "app_name": <app_name>,
    "model_name>": <model_name>,
    "fields_data": <field data of the form {"Field_name": "Field_value", ...}>
  }
  ```
 
 ### Update object
 - Method: put
 - Address: api/rest1/v1/create
 - Options:
 ```javascript
  {
    "app_name": <app_name>,
    "model_name>": <model_name>,
    "pk": <key>,
    "fields_data": <field data like {"field_name": "field_value", ...}>
  }
 ```
 
 ### Deleting an object
 - Method: delete
 - Address: api/rest/v1/delete/<application name>/<model name>/<object_key>'
 
 ### Testing
 python manage.py test auto_api
