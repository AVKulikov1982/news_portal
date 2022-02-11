from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic, View
from django.views.generic import FormView
from django.contrib.auth.models import AnonymousUser

from .forms import CommentForm, NewsForm, UpdateNewsForm
from .models import News, Comment


def home_page(request):
	return render(request, 'app_news/home.html')


class NewsListView(generic.ListView):
	model = News
	template_name = 'app_news/news_list.html'
	context_object_name = 'news_list'
	queryset = News.objects.all()


class NewsDetailView(generic.DetailView, FormView):
	model = News
	template_name = 'app_news/news_detail.html'
	form_class = CommentForm

	def get_context_data(self, **kwargs):
		context = super(NewsDetailView, self).get_context_data(**kwargs)
		return context

	def post(self, request, *args, **kwargs):
		comment_form = CommentForm(request.POST)
		comment = Comment()
		if request.user.is_anonymous:
			if comment_form.is_valid():
				comment.username = comment_form.cleaned_data['username'] + '-Anon'
				comment.comment = comment_form.cleaned_data['comment']
				comment.news = News.objects.get(id=int(request.path.split('/')[-1]))
		else:
			comment.username = request.user
			comment.comment = request.POST['comment']
		comment.news = News.objects.get(id=int(request.path.split('/')[-1]))
		comment.save()
		return redirect(request.path)


class CreateNewsFormView(View):

	@staticmethod
	def get(request):
		news_form = NewsForm()
		return render(request, 'app_news/create_news.html', context={'news_form': news_form})

	@staticmethod
	def post(request):
		news_form = NewsForm(request.POST)
		if news_form.is_valid():
			news = News()
			news.title = news_form.cleaned_data['title']
			news.content = news_form.cleaned_data['content']
			news.save()
			return HttpResponseRedirect('/')
		return render(request, 'app_news/create_news.html', context={'news_form': news_form})


class SelectNewsListView(generic.ListView):
	model = News
	template_name = 'app_news/select_news.html'
	context_object_name = 'news_list'
	queryset = News.objects.all()


class UpdateNewsView(View):

	@staticmethod
	def get(request, news_id):
		news = News.objects.get(id=news_id)
		news_form = UpdateNewsForm(instance=news)
		return render(request, 'app_news/update_news.html', context={'news_form': news_form, 'news_id': news_id})

	@staticmethod
	def post(request, news_id):
		news = News.objects.get(id=news_id)
		news_form = UpdateNewsForm(request.POST, instance=news)
		if news_form.is_valid():
			news.save()
		# return render(request, 'app_news/update_news.html', context={'news_form': news_form, 'news_id': news_id})
		return HttpResponseRedirect('/')
