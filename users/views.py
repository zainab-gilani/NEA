from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def login_view(request):
    form = LoginForm

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print("Username", username)
            print("Password", password)

    return render(request, "users/login.html")
#enddef