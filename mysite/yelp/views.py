# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Business, User
# Create your views here.


def home(request):
	business_list = Business.objects.all()[0:10]
	context = {'business_list': business_list}
        return render(request, 'yelp/index.html', context)
