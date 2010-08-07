from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from tagging.views import tagged_object_list

from freamware.models import Picture

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^~(?P<username>[^/]+)/$',                             'freamware.views.profile',        name='freamware_profile'),
	url(r'^~(?P<username>[^/]+)/pictures/$',                    'freamware.views.picture_list',   name='freamware_user_picture_list'),
	url(r'^~(?P<username>[^/]+)/pictures/(?P<picture>[^/]+)/$', 'freamware.views.picture_detail', name='freamware_user_picture_detail'),
	
	url(r'^~(?P<username>[^/]+)/pictures/(?P<picture>[^/]+)/\+save_tags$',
			'freamware.views.save_tags', name='freamware_picture_save_tags'),
	
	url(r'^~(?P<username>[^/]+)/tags/$',                        'freamware.views.tag_list',       name='freamware_user_tag_list'),
#	url(r'^~(?P<username>[^/]+)/tags/(?P<tag>[^/]+)/$',         'freamware.views.tag_detail',     name='freamware_user_tag_detail'),


	url(r'^upload/$', 'django.views.generic.simple.direct_to_template', {'template': 'freamware/upload.html'}),
	url(r'^pictures/$',            'freamware.views.picture_list',   name='freamware_picture_list'),
	url(r'^tags/$',                'freamware.views.tag_list',       name='freamware_tag_list'),

    url(r'^tags/(?P<tag>[^/]+)/$', tagged_object_list,
		dict(queryset_or_model=Picture, paginate_by=10, allow_empty=True, template_object_name='tags'), name='tag_detail'),

    (r'^accounts/login/$',  'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^accounts/change_password/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/change_password/done/$', 'django.contrib.auth.views.password_change_done'),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
