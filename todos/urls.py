from django.urls import path
from .views import (
    todo_list,
    todo_create,
    todo_update,
    todo_delete,
)

urlpatterns = [
    path('', todo_list, name='todo-list'),
    path('create/', todo_create, name='todo-create'),
    path('<int:pk>/update/', todo_update, name='todo-update'),
    path('<int:pk>/delete/', todo_delete, name='todo-delete'),
]
