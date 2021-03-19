from django.urls import path
from . import views

app_name = 'novels'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:novel_id>', views.detail, name='detail'),
    path('create/', views.novel_create, name='novel_create'),
]
