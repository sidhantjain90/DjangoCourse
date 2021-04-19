from django.urls import path
from AppTwo import views

urlpatterns = [
    path('',views.userExtension,name='users'),
]
