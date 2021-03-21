from django.urls import path
from .views import user_login, user_logout, user_register

app_namee = 'accounts'

urlpatterns = [
    path('login/', user_login , name='login'),
    path('register/', user_register , name='register'),
    path('logout/', user_logout, name='logout'),
]