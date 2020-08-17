from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'second_name', 'third_name',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
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
        )}),
        (_('Permissions'), {'fields': ('is_active',
                                       'is_staff',
                                       'is_superuser',
                                       'groups',
                                       'user_permissions',

                                )}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',
                       'password1',
                       'password2',
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
                    )}
        ),
    )
    search_fields = ('username',)
    ordering = ('first_name',)


admin.site.register(CustomUser, CustomUserAdmin)