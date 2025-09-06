from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)


class SkinCancer(models.Model):
    patient = models.CharField(max_length=10)
    image = models.ImageField(_("Image"), upload_to=upload_to)
    nv = models.IntegerField()
    mel = models.IntegerField()
    bkl = models.IntegerField()
    bcc = models.IntegerField()
    akiec = models.IntegerField()
    vasc = models.IntegerField()
    df = models.IntegerField()

    # nv = models.DecimalField(max_digits=3, decimal_places=2, null=True,)
    # mel = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # bkl = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # bcc = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # akiec = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # vasc = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    # df = models.DecimalField(max_digits=3, decimal_places=2, null=True)