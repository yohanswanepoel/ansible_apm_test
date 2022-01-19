from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class Preferences(models.Model):
    notifications = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, verbose_name=_("Owner"), related_name='%(class)s_owner')