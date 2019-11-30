from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signup, name='signin'),
    path('signout/', views.signup, name='signout')
]