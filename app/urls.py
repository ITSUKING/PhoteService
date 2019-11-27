from django.urls import path

from app import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
]
