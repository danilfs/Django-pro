from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
  #Это url самого приложения app,если в первом параметре указать значение, например "hello", то оно будет всегда идти после главного "myapp", главные url находятся в mysite/mysite/urls

  # http://127.0.0.1:8000/myapp/hello
  path('register/', register, name='register'),
  path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
  
  
]