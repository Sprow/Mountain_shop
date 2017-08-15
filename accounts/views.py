from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import LoginForm, RegistrationForm
from accounts.models import User


@login_required(login_url="/login/")
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(username=data.get("username"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    print("sorry")
        return render(request, "login.html", {"form": form})


def registerate_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                password1 = data.get('password1')
                password2 = data.get('password2')
                if User.objects.filter(username=data.get("username")):
                    username_error = 'User with this username is already exists'
                    return render(request, 'registration.html', {"form": form, "username_error": username_error})
                else:
                    if password1 != password2:
                        pass_error = "Passwords don't match"
                        return render(request, 'registration.html', {"form": form, "pass_error": pass_error})
                    else:
                        user = User.objects.create_user(username=data.get("username"),
                                                        email=data.get("email"))
                        user.set_password(password1)
                        user.save()
                        return HttpResponseRedirect(reverse("login"))
        return render(request, 'registration.html', {"form": form})
