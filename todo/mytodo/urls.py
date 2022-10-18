from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.List, name='list'),
    path('detail/<int:todo_id>/', views.Detail, name='detail'),
    path('update/<int:todo_id>/', views.Update, name ='update'),
    path('create/', views.Create, name ='create'),
    path('delete/<int:todo_id>/', views.Delete, name ='delete'),
]
