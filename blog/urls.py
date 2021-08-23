from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:picture_type>/', views.image, name = 'image')
]
