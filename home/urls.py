from django.urls import path
from home import views

urlpatterns = [
    path('',views.add_task,name = 'add_task'),
    path('tasks/',views.task,name = 'tasks'),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('update_task/<str:pk>', views.update, name = "update"),
    path('view_task/<str:pk>', views.view_task, name = "view_task"),
    path('about/', views.about, name = "about"),
]