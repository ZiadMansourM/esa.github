from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator



# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(_('first name'), max_length=30)
    second_name = models.CharField(_('second name'), max_length=30)
    third_name = models.CharField(_('third name'), max_length=30)

    num_posts = models.IntegerField(_('Number of Posts'), default=0,)
    num_reactions = models.IntegerField(_('Number of Reactions'), default=0,)
    num_shares = models.IntegerField(_('Number of Shares'), default=0,)
    num_posts_month = models.IntegerField(_('Number of Posts-Month'), default=0,)
    num_reactions_post = models.IntegerField(_('Number of Reactions-Post'), default=0,)
    num_shares_post = models.IntegerField(_('Number of Shares-Post'), default=0,)
    missed = models.IntegerField(_('Missed'), default=0,)
    met = models.IntegerField(_('Met'), default=0,)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )


    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


    objects = CustomUserManager()

    REQUIRED_FIELDS = [
        'first_name',
        'second_name',
        'third_name',
    ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'esa_vol'

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.third_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


    def __str__(self):
        return self.first_name + " " + self.third_name 
