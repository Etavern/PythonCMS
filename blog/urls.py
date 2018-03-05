from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^reset_password/$', views.reset_password, name='reset_password'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'post_delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^account/$', views.account, name='account'),
]
