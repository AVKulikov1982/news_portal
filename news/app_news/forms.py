from django import forms

from .models import News


class CommentForm(forms.Form):
	username = forms.CharField()
	comment = forms.CharField()


class NewsForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField()


class UpdateNewsForm(forms.ModelForm):

	class Meta:
		model = News
		fields = ['title', 'content', 'flag']
