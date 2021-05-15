from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index, name="list"),
    path('update/<str:pk>/',views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete_task"),
]