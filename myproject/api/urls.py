from django.urls import path
from . import views

# app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.tasklist, name='task-list'),
    path('task-create/', views.taskcreate, name='task-create'),
    path('task-detail/<str:pk>/', views.taskdetail, name='task-detail'),
    path('task-update/<str:pk>/', views.taskupdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskdelete, name='task-delete'),
]