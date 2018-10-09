from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='landing'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^upload/$', views.new_post, name='newPost'),
    url(r'^likes/$', views.like_post, name='like_post'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^follow/(\d+)$', views.follow, name='follow'),
    url(r'^unfollow/(\d+)$', views.unfollow, name='unfollow'),
    url(r'^search/$', views.search_user, name='search_profile'),
    url(r'^comment/(?P<image_id>\d+)', views.add_comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)