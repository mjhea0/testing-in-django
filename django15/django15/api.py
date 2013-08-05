from tastypie.resources import ModelResource
from tastypie.constants import ALL
from whatever.models import Whatever

class WhateverResource(ModelResource):
	class Meta:
		queryset = Whatever.objects.all()
		resource_name = 'whatever'
		filtering = { "title" : ALL }