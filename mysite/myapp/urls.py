from django.urls import path
from myapp.views import index,indexItem

app_name = "myapp"

urlpatterns = [
  #Это url самого приложения app,если в первом параметре указать значение, например "hello", то оно будет всегда идти после главного "myapp", главные url находятся в mysite/mysite/urls

  # http://127.0.0.1:8000/myapp/hello
  path('', index),
  path('<int:my_id>/', indexItem, name="detail"),
  # http://127.0.0.1:8000/myapp/contacts
  
]