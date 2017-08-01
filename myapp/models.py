# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    is_released = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('view_not_released', 'Can see my models that are not released.'),
        )
