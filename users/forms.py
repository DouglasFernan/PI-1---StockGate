from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "name", "cpf", "groups", "profile_picture")
        # '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        # Se nenhum valor for enviado para profile_picture, usa o padrão
        if not user.profile_picture:
            user.profile_picture = 'profile_pictures/default.jpg'
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
