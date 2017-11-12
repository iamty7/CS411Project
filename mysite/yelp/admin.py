# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Business, User, Comment
# Register your models here.

admin.site.register(Business)

admin.site.register(User)

admin.site.register(Comment)
