from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _

ACTIVE_STATUS = (
    (0, _('Inactive')),
    (1, _('Active')),
    (2, _('Pending Approval'))
)


class CategoryManager(models.Manager):
    def is_active(self):
        return super(CategoryManager, self).get_queryset().filter(active=1)


class Category(models.Model):
    name = models.CharField(_('Category name'),
                            max_length=50, null=False, blank=False)
    active = models.BooleanField(_('Active'), choices=ACTIVE_STATUS, default=2)
    objects = CategoryManager()

    def __unicode__(self):
        return self.name

    def is_active(self):
        return self.active == 1

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
