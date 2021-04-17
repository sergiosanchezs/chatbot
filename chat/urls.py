from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
]