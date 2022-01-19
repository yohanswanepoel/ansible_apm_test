from django.db import models
from django.utils.translation import ugettext_lazy as _
from myaccounts.users.models import User


class Accounts(models.Model):
    number = models.CharField(verbose_name=_("Acc Number"), max_length=50)
    name = models.CharField(verbose_name=_("Acc Name"), max_length=50)
    display_name = models.CharField(verbose_name=_("Display Name"), max_length=50)
    balance = models.DecimalField(verbose_name=_("Balance"), max_digits=10, decimal_places=2)
    balance_date = models.DateTimeField(verbose_name=_("Date Updated"), auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name=_("Owner"), related_name='%(class)s_owner')

    # Adding some documentation
    # Testing comments
    def __str__(self):
        return self.display_name
