from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _

ACTIVE_STATUS = (
    (0, _('Inactive')),
    (1, _('Active')),
    (2, _('Pending Approval'))
)


class Category(models.Model):
    name = models.CharField(_('Category name'),
                            max_length=50, null=False, blank=False)
    active = models.BooleanField(_('Active'), choices=ACTIVE_STATUS, default=2)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
