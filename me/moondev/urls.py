from django.urls import path
from . import views

app_name = 'moondev'

urlpatterns = [
    path('printers/', views.printer_list, name='printer_list'),
    path('printers/<int:printer_id>/', views.printer_detail, name='printer_detail'),
    path('jobs/', views.print_job_list, name='print_job_list'),
]

