from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksList.as_view()),
    path('create/', views.TasksCreate.as_view()),
    path('edit/<int:pk>', views.TasksUpdate.as_view()),
    path('delete/<int:pk>', views.TasksDelete.as_view()),
]
