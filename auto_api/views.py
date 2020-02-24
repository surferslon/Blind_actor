import json
from django.apps import apps
from django.db.utils import IntegrityError
from django.core.exceptions import FieldDoesNotExist, FieldError
from rest_framework.views import APIView
from rest_framework.response import Response


def get_model_or_400(data):
    try:
        return apps.get_model(
            data.get('app_name', ''),
            data.get('model_name', '')
        )
    except LookupError as e:
        return Response(str(e), status=400)


class ListView(APIView):

    def get(self, request, *args, **kwargs):
        data = []
        for model in apps.get_models():
            data.append({'model': model.__name__, 'fields': [model_field.name for model_field in model._meta.fields]})
        return Response(data)


class SearchView(APIView):

    def get(self, request, *args, **kwargs):
        model = get_model_or_400(kwargs)
        if isinstance(model, Response):
            return model
        order_by = request.GET.get('order_by', 'id')
        try:
            model._meta.get_field(order_by)
        except FieldDoesNotExist as e:
            return Response(str(e), status=400)
        limit = request.GET.get('limit')
        limit = int(limit) if limit else None
        search = request.GET.get('search', '{}')
        try:
            search = json.loads(search)
        except json.decoder.JSONDecodeError as e:
            return Response(f'invalid search parameter: {str(e)}', status=400)
        try:
            qs = model.objects.filter(**search).order_by(order_by)[:limit]
        except (FieldError, TypeError, ValueError, FieldError) as e:
            return Response(str(e), status=400)
        response_data = []
        for item in qs:
            item_dict = {}
            for field in model._meta.fields:
                item_dict[field.name] = str(getattr(item, field.name))
            response_data.append(item_dict)
        return Response(response_data)


class CreateView(APIView):

    def post(self, request):
        model = get_model_or_400(request.data)
        if isinstance(model, Response):
            return model
        instance_data = request.data.get('fields_data')
        try:
            instance_data = json.loads(instance_data)
        except json.decoder.JSONDecodeError as e:
            return Response(str(e), status=400)
        try:
            model.objects.create(**instance_data)
        except (TypeError, ValueError, IntegrityError) as e:
            return Response(str(e), status=400)

        return Response(status=201)


class UpdateView(APIView):

    def put(self, request, format=None):
        model = get_model_or_400(request.data)
        if isinstance(model, Response):
            return model
        instance_data = request.data.get('fields_data')
        instance_pk = request.data.get('pk', None)
        try:
            model.objects.get(pk=instance_pk)
        except model.DoesNotExist as e:
            return Response(str(e), 400)
        try:
            instance_data = json.loads(instance_data)
        except json.decoder.JSONDecodeError as e:
            return Response(str(e), status=400)
        try:
            updated = model.objects.filter(pk=instance_pk).update(**instance_data)
        except FieldDoesNotExist as e:
            return Response(str(e))
        return Response(f'{updated} updated', status=200)


class DeleteView(APIView):

    def get(self, request, *args, **kwargs):
        model = get_model_or_400(kwargs)
        if isinstance(model, Response):
            return model
        instance_pk = kwargs.get('pk', None)
        try:
            model.objects.get(pk=instance_pk)
        except model.DoesNotExist as e:
            return Response(str(e), 400)
        return Response()

    def delete(self, request, *args, **kwargs):
        model = get_model_or_400(kwargs)
        if isinstance(model, Response):
            return model
        instance_pk = kwargs.get('pk', None)
        try:
            model.objects.get(pk=instance_pk)
        except model.DoesNotExist as e:
            return Response(str(e), 400)
        try:
            deleted = model.objects.filter(pk=instance_pk).delete()
        except FieldDoesNotExist as e:
            return Response(str(e))
        return Response(f'{deleted} deleted', status=200)
