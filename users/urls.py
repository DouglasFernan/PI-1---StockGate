from django.views.generic import FormView
from django.urls import path
from . import views
from . import forms
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('registration/', views.UserRegistration.as_view(), name='registration' ),
    path('ceo/dashboard/', views.ceo_dashboard, name='ceo_dashboard'),
    path('ceo/historico_de_vendas/', views.ceo_historico_de_vendas, name="historico_de_vendas"),
    path('ceo/gerenciar_usuarios/', views.UsersListView. as_view(), name="gerenciar_usuarios"),
    path('ceo/gerenciar_produtos/', views.ceo_gerenciar_produtos, name="gerenciar_produtos"),
    path('ceo/gerenciar_categorias/', views.ceo_gerenciar_categorias, name="gerenciar_categorias"),
    path('ceo/fornecedores/', views.ceo_fornecedores, name="fornecedores"),
    path('gerente/dashboard/', views.gerente_dashboard, name='gerente_dashboard'),
    path('gerente/gerenciar_categorias/', views.gerente_gerenciar_categorias, name="gerente_gerenciar_categorias"),
    path('vendedor/registrar_vendas/', views.vendedor_registrar_vendas, name="vendedor_registrar_vendas"),
    path('vendedor/dashboard/', views.vendedor_dashboard, name='vendedor_dashboard'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
