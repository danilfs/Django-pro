from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("form is valid:", form.is_valid()) #Отладочный вывод
        if form.is_valid():
            user = form.save()
            print("User saved:", user) #Отладочный вывод
            messages.success(request, "Registration successful!")
        else:
            print(form.errors) #Отладочный вывод - покажет ошибки валидации
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)
# Create your views here.

# from .forms import NewUserForm
# from django.shortcuts import render

# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#     form = NewUserForm()
#     context = {"form": form}
#     return render(request, "users/register.html", context)


