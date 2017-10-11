# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import ResourceType


# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"
        ]
        super(CustomAdmin, self).__init__(model, admin_site)



admin.site.register(ResourceType, CustomAdmin)
