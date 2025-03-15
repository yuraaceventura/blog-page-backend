from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blogs/<int:item_id>', views.blog, name='blog'),
    path('blogs/delete/<int:item_id>', views.delete, name="delete"),
    path('blogs/update/<int:item_id>', views.update, name="update"),
    path('blogs/create', views.create, name='create'),
    path('blogs/', views.index, name='index'),
]