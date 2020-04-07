from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
        Extends froms Django Abstract User to change
        the username filed and add extra fields
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +99999999, up to 15 digits allowed'
    )
    phone_number = models.CharField(
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Helps to classify users'
            'Cients are the main type of user'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user has verified the email address'
    )

    def __str__(self):

        return self.username

    def get_short_name(self):

        return self.username