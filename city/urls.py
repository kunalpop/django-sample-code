from .views import ListCitiesView,CrudView
from django.urls import path

urlpatterns = [
    path('cities/all', ListCitiesView.as_view(), name='cities-list'),
    path('cities/<str:unloc_code>', CrudView.as_view(), name='cities-crud'),
]