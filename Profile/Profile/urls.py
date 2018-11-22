"""Profile URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^$', views.Index,name='index'),
    #url('',include('basic_app.urls')),
    url(r'^show/',views.show,name="show"),

    url(r'^insert/',views.insert,name="insert"), 
    url(r'^hii/(?P<pk>\d+)/$',views.hii,name="hii"),  
    url(r'^$',views.home,name="home"),
    url(r'^student/',views.unauth,name="student"),

     url(r'^view/(?P<pk>\d+)/$',views.view,name="view"),

    url(r'^create/',views.create_product,name="create_product"),
   # url(r'^update/<int:id>',views.update,name="update"),

    url(r'^update/(?P<pk>\d+)/$',views.update,name="update"),

    #(r'^edit/(?P<pk>\d+)/$',views.edit,name="edit"),
    url(r'^delete/(?P<pk>\d+)/$',views.delete,name="delete"),
      url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
