from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'second_name',
            'third_name',
            'num_posts',
            'num_reactions',
            'num_shares',
            'num_posts_month',
            'num_reactions_post',
            'num_shares_post',
            'missed',
            'met',
            'is_staff',
            'is_active'
        )