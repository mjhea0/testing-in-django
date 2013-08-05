from django import forms
from models import Whatever

class WhateverForm(forms.ModelForm):

	class Meta:
		model = Whatever
		fields = ('title', 'body')