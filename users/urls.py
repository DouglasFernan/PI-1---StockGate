from django.views.generic import FormView
from django.urls import path
from . import views
from . import forms
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('ceo/dashboard/', views.ceo_dashboard, name='ceo_dashboard'),
    path('gerente/dashboard/', views.gerente_dashboard, name='gerente_dashboard'),
    path('vendedor/dashboard/', views.vendedor_dashboard, name='vendedor_dashboard'),
    path('registration/', views.UserRegistration.as_view(), name='registration' ),
    path('usuarios/', views.UsersListView. as_view(), name="usuarios"),
    path('gerenciar_produtos/', views.gerenciar_produtos, name="gerenciar-produtos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
