from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from . import forms


# Create your views here.
# ceo = CustomUser.objects.create(email="douglasgenetic@gmail.com",
#                                 name="Douglas Fernandes", cpf="13359863402")
# ceo.set_password("Pass@2024")
# ceo.groups.add(Group.objects.get(name="CEO"))
# ceo.save()


def get_dashboard_url(user):
    group_dashboard_map = {
        'CEO': 'ceo_dashboard',
        'Gerente': 'gerente_dashboard',
        'Vendedor': 'vendedor_dashboard',
    }
    user_group = user.groups.first().name
    return group_dashboard_map[user_group]
    # for group, dashboard_url in group_dashboard_map.items():
    #     if user.groups.filter(name=group).exists():
    #         return dashboard_url
    # return ''


def login_view(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # print(user, username, password,)
        # breakpoint()
        if user is not None:
            login(request, user)
            return redirect(get_dashboard_url(user))
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect("login")


class UserRegistration(FormView):
    form_class = forms.CustomUserCreationForm
    template_name = "users/registration.html"


@login_required
def ceo_dashboard(request):
    return render(request, 'users/ceo/index.html')


@login_required
def gerente_dashboard(request):
    return render(request, 'users/gerente/index.html')


@login_required
def vendedor_dashboard(request):
    return render(request, 'users/vendedor/index.html')
