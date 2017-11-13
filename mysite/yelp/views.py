# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone

from .models import Business, User, Comment
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


def delete_comment(request):
	comment_text = request.POST.get('comment_text');
	comment = get_object_or_404(Comment, comment_text = comment_text)
        #comment = Comment.objects.get(comment_text=comment_text)
	business = comment.business
	comment.delete()
	return redirect(business_detail, business_id = business.id)


def update_comment(request):
	comment_id = request.POST.get('comment_id');
        comment_text = request.POST.get('comment_text');
	comment = get_object_or_404(Comment, pk=comment_id)
	comment.comment_text = comment_text
	comment.comm_date = timezone.now()
        comment.save()
	business = comment.business
	return redirect(business_detail, business_id = business.id)

#def delete_comment(request, comment_id):
#	comment = get_object_or_404(Comment, pk=comment_id)
#   business = comment.business
#	comment.delete()
	#return render(request, 'yelp/business.html', {'business': business})
#        return redirect(business_detail, business_id = business.id)
