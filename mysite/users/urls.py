from django.urls import path
from .views import register, profile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import seller_profile



app_name = "users"

urlpatterns = [
  #Это url самого приложения app,если в первом параметре указать значение, например "hello", то оно будет всегда идти после главного "myapp", главные url находятся в mysite/mysite/urls

  # http://127.0.0.1:8000/myapp/hello
  path('register/', register, name='register'),
  path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
  path("logout/", views.logout_view, name="logout"),
  path("profile/", profile, name="profile"),
  path("sellerprofile/<int:id>", seller_profile, name="sellerprofile"),
  # path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  
  
]