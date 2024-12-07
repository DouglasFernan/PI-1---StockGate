from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# ceo = CustomUser.objects.create(email="douglasgenetic@gmail.com",
#                                 name="Douglas Fernandes", cpf="13359863402")
# ceo.set_password("Pass@2024")
# ceo.groups.add(Group.objects.get(name="CEO"))
# ceo.save()


def login_view(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        # Redirect to a success page.
        ...
    else:
        return render(request, 'users/login.html')
        # Return an 'invalid login' error message.
        ...


def logout_view(request):
    logout(request)
    return redirect("login")


def index(request):
    return render(request, 'users/index.html')
