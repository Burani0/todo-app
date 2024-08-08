
from django.urls import path
from django.contrib.auth import views as auth_views
from todoapp import views 
from django.contrib import admin
from .import views
from .views import *







aap_name="todoapp"


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/new/', views.todo_create, name='todo_create'),
    path('todo/<int:pk>/edit/', views.todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]