# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Business, User
# Create your views here.


def home(request):
	#business_list = Business.objects.all()[0:10]
	#context = {'business_list': business_list}
        return render(request, 'yelp/index.html')


def search_business(request):
	keyword = request.POST.get('keyword')
	error_msg = ''

	if not keyword:
		error_msg = 'Please type your keyword to search!'
		return render(request, 'yelp/searchResults.html', {'error_msg': error_msg})

	business_list = Business.objects.filter(name__icontains = keyword)[0:5]
	return render(request, 'yelp/searchResults.html', {'business_list': business_list, 'error_msg': error_msg})


def business_detail(request, business_id):
	try:
		business = Business.objects.get(pk = business_id)
	except Business.DoesNotExist as e:
		raise Http("Business does not exist!")
	
	return render(request, 'yelp/business.html', {'business': business})

def delete_comment(request, comment_id, business.id):
	comment = get_object_or_404(Comment, pk=comment_id)
	comment.delete()
	return render(request, 'yelp/business.html', {'business': business})