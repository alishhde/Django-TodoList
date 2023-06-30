from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path("update/<int:pk>/", views.update_task_view, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]
