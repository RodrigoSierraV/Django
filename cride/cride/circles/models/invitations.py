from django.db import models

from cride.utils.models import CRideModel
from cride.circles.managers import InvitationManager

class Invitation(CRideModel):
    """
        Unique code that grants access to a specific circle.
        This code can be generated by an active member of the circle
        with remaining invitations
    """

    code = models.CharField(max_length=50, unique=True)
    issued_by = models.ForeignKey(
        'users.User',
        on_delete= models.CASCADE,
        help_text='Member that provides the invitation',
        related_name='issued_by'
    )
    used_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        help_text='User that uses the code'
    )

    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(blank=True, null=True)

    objects = InvitationManager()

    def __str__(self):
        return f'#{self.circle.slug_name}: {self.code}' 