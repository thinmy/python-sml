from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.db import models
from django.utils.translation import gettext as _


from categories.models import Category

STATUS_CHOICES = (
    (0, _('Public')),
    (1, _('Private'))
)

ACTIVE_STATUS = (
    (0, _('Inactive')),
    (1, _('Active'))
)


class TourManager(models.Manager):
    def is_active(self):
        return super(TourManager, self).get_queryset().filter(active=1)


class Tour(models.Model):
    active = models.BooleanField(_('Active'), choices=ACTIVE_STATUS, default=1)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_('Category'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    latitude = models.FloatField(_('Latitude'), null=False, blank=False)
    longitude = models.FloatField(_('Longitude'), null=False)
    name = models.CharField(_('Name'), max_length=255, blank=False)
    type = models.IntegerField(_('Type'), choices=STATUS_CHOICES, default=0)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name=_('Owner'))

    objects = TourManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tours'
