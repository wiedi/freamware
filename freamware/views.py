from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic.list_detail import object_list, object_detail
from django.template import RequestContext
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from tagging.models import Tag
from tagging.utils import edit_string_for_tags

from django.contrib.auth.models import User
from models import Picture

def profile(request, username):
	u = get_object_or_404(User, username = username)
	return render_to_response("freamware/profile.html",
			{'user': u}, context_instance = RequestContext(request))


def picture_detail(request, username, picture):
	p = get_object_or_404(Picture, slug = picture)
	return render_to_response("freamware/picture.html",
			{'picture': p, 'tags': edit_string_for_tags(p.tags)}, context_instance = RequestContext(request))
			
			
def picture_list(request, username = None):
	if username:
		qs = Picture.objects.filter(user__username = username)
	else:
		qs = Picture.objects.all()
	return object_list(request, qs, template_name='freamware/picture_list.html')
	

	
def tag_list(request, username = None):
	return render_to_response("freamware/tags.html",
			{}, context_instance = RequestContext(request))


@login_required
def save_tags(request, username, picture):
	p = get_object_or_404(Picture, slug = picture)
	if p.user != request.user:
		return redirect_to_login(reverse(picture_detail, args=[username, picture]))
	if request.method == 'POST':
		Tag.objects.update_tags(p, request.POST['tags'])
	return redirect('freamware_user_picture_detail', username=username, picture=picture)	
	
