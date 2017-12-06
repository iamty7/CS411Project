# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django import forms

from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext  

from .models import Business, Comment #, User
import json
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

	business_list = Business.objects.filter(name__icontains = keyword)[0:9]
	return render(request, 'yelp/searchResults.html', {'business_list': business_list, 'error_msg': error_msg})

#@csrf_exempt
def search_suggestion(request):
	keyword = request.GET.get('keyword')
	if keyword:
		business_list = Business.objects.filter(name__icontains = keyword)[0:5]
		rejson = []
		for business in business_list:
        		rejson.append(business.name)
    		return HttpResponse(json.dumps(rejson), content_type='application/json')
		#return HttpResponse(rejson)

def business_detail(request, business_id):
	try:
		business = Business.objects.get(pk = business_id)
	except Business.DoesNotExist as e:
		raise Http("Business does not exist!")
	
	return render(request, 'yelp/business.html', {'business': business})


def delete_comment(request):
	comment_id = request.POST.get('comment_id')
	comment = get_object_or_404(Comment, pk = comment_id)
        #comment = Comment.objects.get(comment_text=comment_text)
	business = comment.business
	comment.delete()
	return redirect(business_detail, business_id = business.id)


def update_comment(request):
	comment_id = request.POST.get('comment_id')
    	comment_text = request.POST.get('comment_text')
	comment = get_object_or_404(Comment, pk=comment_id)
	comment.comment_text = comment_text
	comment.comm_date = timezone.now()
    	comment.save()
	business = comment.business
	return redirect(business_detail, business_id = business.id)

def add_comment(request):
	business_id = request.POST.get('business_id')
    	comment_text = request.POST.get('comment_text')
    	business = Business.objects.get(pk=business_id)
    	business.comment_set.create(comment_text=comment_text,comm_date=timezone.now())

	return redirect(business_detail, business_id = business_id)



#def delete_comment(request, comment_id):
#	comment = get_object_or_404(Comment, pk=comment_id)
#   business = comment.business
#	comment.delete()
	#return render(request, 'yelp/business.html', {'business': business})
#        return redirect(business_detail, business_id = business.id)


def login(request):  
    form = UserForm(request.POST)  
	if form.is_valid():  
        username = request.POST.get('username', '')  
        password = request.POST.get('password', '')  
        user = auth.authenticate(username=username, password=password)  
        if user is not None and user.is_active:  
        	auth.login(request, user)  
            return render_to_response('login.html', RequestContext(request))  
        else:  
            return render_to_response('index.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
    else:  
            return render_to_response('index.html', RequestContext(request, {'form': form,}))  

class UserForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
        label=u"username",  
        error_messages={'required': 'Your username please'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"username",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"password",  
        error_messages={'required': u'Your password please'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"username and password are necessary")  
        else:  
            cleaned_data = super(UserForm, self).clean()   


def signup(request):
    curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
   


    if request.method == "POST":
    	username = request.POST.get('username')
    	email = request.POST.get('email')
    	if len(django.contrib.auth.models.User.objects.filter(username = username)) > 0:
    		error_msg = "Username exits!!"
    		return render(request, 'yelp/index.html',{'error_msg': error_msg})
    	elif not email:
    		error_msg = "Email please!"
    		return render(request, 'yelp/index.html',{'error_msg': error_msg})
    	else:
    		password = request.POST.get('password')
    		password_confirmation = request.POST.get('password_confirmation')
    		if password != password_confirmation:
    			error_msg = "Passwords do not match!"
    			return render(request, 'yelp/index.html',{'error_msg': error_msg})
    		else:
    			user = django.contrib.auth.models.User.objects.create_user(username, email, password)
    			user.save()
    error_msg = "Sign up successfully!!!"
	return render(request, 'yelp/index.html',{'error_msg': error_msg})



@login_required  
def logout(request):  
    auth.logout(request)  
    return redirect(home)