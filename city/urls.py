from .views import ListCitiesView,CrudView
from django.urls import path
from city.swagger import schema_view

urlpatterns = [
    path('cities/all', ListCitiesView.as_view(), name='cities-list'),
    path('cities/<str:unloc_code>', CrudView.as_view(), name='cities-crud'),
    path('swagger', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
]