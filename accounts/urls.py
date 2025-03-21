from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
