import json
from django.test import TestCase
from django.urls import reverse
from django.apps import apps
from auto_api.models import TestModel
from rest_framework.test import APITestCase


class TestListViews(TestCase):

    def test_get_models_list(self):
        response = self.client.get(reverse('auto_api:list'))
        apps_count = len(apps.get_models())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), apps_count)


class TestSearchView(TestCase):

    def test_search_object(self):
        char_field_value = 'asdf'
        TestModel.objects.create(char_field=char_field_value, int_field=123, float_field=1.11)
        params_string = '?search={"char_field": "asdf", "int_field":123}'
        url = reverse('auto_api:search', kwargs={
            'app_name': TestModel._meta.app_label,
            'model_name': TestModel._meta.model_name}
        )
        response = self.client.get(f'{url}{params_string}')
        self.assertEqual(response.json()[0]['char_field'], char_field_value)
        self.assertEqual(response.json()[0]['id'], 1)


class TestCreateView(TestCase):

    def test_create_object(self):
        fields_data = {
            "char_field": "asdf",
            "int_field": 123,
            "float_field": 1.11
        }
        response = self.client.post(
            reverse('auto_api:create'),
            {
                'app_name': TestModel._meta.app_label,
                'model_name': TestModel._meta.model_name,
                'fields_data': json.dumps(fields_data)
            }
        )
        created_model = TestModel.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(created_model.char_field, fields_data['char_field'])
        self.assertEqual(created_model.int_field, fields_data['int_field'])
        self.assertEqual(created_model.float_field, fields_data['float_field'])


class TestUpdateView(APITestCase):

    def test_update_object(self):
        new_object = TestModel.objects.create(char_field='asdf', int_field=123, float_field=1.11)
        new_value = 'qwer'
        response = self.client.put(
            reverse('auto_api:update'),
            {
                'app_name': TestModel._meta.app_label,
                'model_name': TestModel._meta.model_name,
                'pk': new_object.pk,
                'fields_data': json.dumps({'char_field': new_value})
            }
        )
        new_object.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_object.char_field, new_value)


class TestDeleteView(APITestCase):

    def test_delete(self):
        new_object = TestModel.objects.create(char_field='asdf', int_field=123, float_field=1.11)
        object_pk = new_object.pk
        response = self.client.delete(
            reverse(
                'auto_api:delete',
                kwargs={
                    'app_name': TestModel._meta.app_label,
                    'model_name': TestModel._meta.model_name,
                    'pk': new_object.pk,
                }
            ),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(TestModel.objects.filter(pk=object_pk).exists(), False)
