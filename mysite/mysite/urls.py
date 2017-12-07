"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Import view functions from yelp app.
from yelp.views import home, search_business, business_detail, delete_comment, update_comment, add_comment, search_suggestion, logout, signup, login, chatroom_post, chatroom

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^home/$', home, name = 'home'),
    url(r'^search/$', search_business, name = 'search-business'),
    url(r'^searchsuggestion/$', search_suggestion, name = 'search-suggestion'),
    url(r'^deleteComment/$', delete_comment ,name = 'delete-comment'),
    url(r'^updateComment/$', update_comment ,name = 'update-comment'),
    url(r'^addComment/$', add_comment ,name = 'add-comment'),
    #url(r'^deleteComment/(?P<comment_id>\S*)/$', delete_comment ,name = 'delete-comment'),
    url(r'^business/(?P<business_id>\S+)/$', business_detail, name = 'business-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name = 'signup'),  
    url(r'^logout/$', logout, name = 'logout'),  
    url(r'^login/$', login, name = 'login'),  
    url(r'^chatroom/post/$', chatroom_post, name = 'chatroom-post'), 
    url(r'^chatroom/$', chatroom, name = 'chatroom'),

]
