from django.shortcuts import render_to_response
from whatever.models import Whatever
from django.core.context_processors import csrf
from django.utils import timezone
from whatever.forms import WhateverForm
from django.http import HttpResponse, HttpResponseRedirect

def whatever(request):
	args = {}
	args.update(csrf(request))
	args['whatever'] = Whatever.objects.all()

	return render_to_response('index.html', args)

def add(request):
	if request.POST:
		form = WhateverForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = WhateverForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('add.html', args)