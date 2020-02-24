from django.urls import path, include
from . import views


app_name = 'auto_api'
urlpatterns = [
    path('list', views.ListView.as_view(), name='list'),
    path('search/<str:app_name>/<str:model_name>/', views.SearchView.as_view(), name='search'),
    path('create', views.CreateView.as_view(), name='create'),
    path('update', views.UpdateView.as_view(), name='update'),
    path('delete/<str:app_name>/<str:model_name>/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
