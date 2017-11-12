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

def searchBusiness(request):
	keyword = request.GET.get('keyword')
	error_msg = ''

	if not keyword:
		error_msg = 'Please type your keyword to search!'
		return render(request, 'yelp/searchResults.html', {'error_msg': error_msg})

	business_list = Business.objects.fileter(name__icontains = keyword)[0:5]
	return render(request, 'yelp/searchResults.html', {'business_list': business_list, 'error_msg': error_msg})
