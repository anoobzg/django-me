from django.urls import path
from . import views

app_name = 'moonraker'

urlpatterns = [
    path('server/info', views.server_info, name='server_info'),
    path('printer/info', views.printer_info, name='printer_info'),
    path('printer/objects/query', views.printer_objects_query, name='printer_objects_query'),
    path('printer/objects/list', views.printer_objects_list, name='printer_objects_list'),
    path('printer/status', views.printer_status, name='printer_status'),
]

