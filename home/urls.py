from django.urls import path
from home.views import calculate_distance_view

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='calaculate-view'),
]