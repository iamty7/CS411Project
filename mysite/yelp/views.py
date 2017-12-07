# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User as MyUser
from django.db.models import Count

from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext  

from .models import Business, Comment, User, Review, Chat
import json
# Create your views here.



def home(request):
    return render(request, 'yelp/index.html')

def ihome(request, error_msg):
	#business_list = Business.objects.all()[0:10]
	#context = {'business_list': business_list}
    return render(request, 'yelp/index.html',{'error_msg':error_msg})


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
		reviews_of_this_business = Review.objects.filter(business = business, stars__gte = 4)
		users = set(review.user for review in reviews_of_this_business)
		reviews = Review.objects.filter(user__in =  users, stars__gte = 4).exclude(business = business)
		blist = reviews.values('business').annotate(reviewCnt=Count('business')).order_by('-reviewCnt').values('business')

		business_list = Business.objects.filter(pk__in = blist)[0:6]

	except Business.DoesNotExist as e:
		raise Http("Business does not exist!")
	
	return render(request, 'yelp/business.html', {'business': business, 'business_list':business_list})


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
	#form = UserForm(request.POST)  
	#if form.is_valid():  
	username = request.POST.get('username')  
	password = request.POST.get('password')  
	user = auth.authenticate(username=username, password=password)  
	if user is not None and user.is_active:  
		auth.login(request, user) 
		#error_msg = 'Login successfully!!!' 
		#return render(request, 'yelp/index.html', {'error_msg': error_msg})  
		#return render(request, 'yelp/chatroom.html')
		return redirect(chatroom)
	else:  
		error_msg = 'Username or password not correct!!'
		return render(request, 'yelp/index.html', {'error_msg': error_msg})
		#return redirect(home, error_msg = "Username or password not correct!!")


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

@csrf_exempt
def signup(request):
    #curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
   


    if request.method == "POST":
    	username = request.POST.get('username')
    	email = request.POST.get('email')
    	if len(auth.models.User.objects.filter(username = username)) > 0:
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
    			user = auth.models.User.objects.create_user(username, email, password)
    			user.save()
	error_msg = "Sign up successfully!!!"
	return render(request, 'yelp/index.html',{'error_msg': error_msg})



@login_required  
def logout(request):  
    auth.logout(request)  
    return redirect(home)

def chatroom(request):
	try:
		user = MyUser.objects.get(username = request.user)
	except MyUser.DoesNotExist:
		return redirect(home)
	chats = list(Chat.objects.all())[-100:]
	return render(request, 'yelp/chatroom.html', {'chats': chats, 'user': user})

@csrf_exempt
def chatroom_post(request):
    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            new_chat = Chat.objects.create(
                content = request.POST.get('content'),
                sender = request.user,
            )
            new_chat.save()
            return HttpResponse()
        elif post_type == 'get_chat':
            last_chat_id = int(request.POST.get('last_chat_id'))
            chats = Chat.objects.filter(id__gt = last_chat_id)
            return render(request, 'yelp/chat_list.html', {'chats': chats})
    else:
        raise Http404
