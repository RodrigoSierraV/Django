from django.db import models

from cride.utils.models import CRideModel


class Circle(CRideModel):
    """
        Private group where rides are offered an taken by its members
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official comunities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone knows about their existence'
    )
    
    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit of the number of members'
    )

    def __str__(self):

        return self.name
    
    class Meta(CRideModel.Meta):

        ordering = ['-rides_taken', '-rides_offered']