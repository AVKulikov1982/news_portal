from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic, View
from django.views.generic import FormView
from django.contrib.auth.models import AnonymousUser, User, Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from .forms import CommentForm, NewsForm, UpdateNewsForm, FilterForm
from .models import News, Comment


def home_page(request):
	Group.objects.get_or_create(name='moderators')
	Group.objects.get_or_create(name='verified')
	moderators = Group.objects.get(name="moderators").user_set.all()
	verified = Group.objects.get(name="verified").user_set.all()
	return render(request, 'app_news/home.html', context={'moderators': moderators, 'verified': verified})


class NewsListView(View):

	@staticmethod
	def get(request):
		news_list = News.objects.all()
		filter_form = FilterForm()
		return render(request, 'app_news/news_list.html', context={'news_list': news_list, 'filter_form': filter_form})

	@staticmethod
	def post(request):
		filter_form = FilterForm(request.POST)
		if filter_form.is_valid():
			tag = filter_form.cleaned_data.get('tag')
			created_at = filter_form.cleaned_data.get('created_at')
			if tag and not created_at:
				news_list = News.objects.filter(tag=tag)
			elif not tag and created_at:
				news_list = News.objects.filter(created_at=created_at)
			elif tag and created_at:
				news_list = News.objects.filter(tag=tag, created_at=created_at)
			else:
				news_list = News.objects.all()

			return render(request, 'app_news/news_list.html', context={'news_list': news_list})
		else:
			news_list = News.objects.all()
			return render(request, 'app_news/news_list.html', context={'news_list': news_list, 'filter_form': filter_form})


class NewsDetailView(generic.DetailView, FormView):
	model = News
	template_name = 'app_news/news_detail.html'
	form_class = CommentForm

	def get_context_data(self, **kwargs):
		context = super(NewsDetailView, self).get_context_data(**kwargs)
		return context

	@staticmethod
	def post(request):
		comment_form = CommentForm(request.POST)
		comment = Comment()
		if request.user.is_anonymous:
			if comment_form.is_valid():
				comment.username = comment_form.cleaned_data['username'] + '-Anon'
				comment.comment = comment_form.cleaned_data['comment']
				comment.news = News.objects.get(id=int(request.path.split('/')[-1]))
		else:
			comment.username = request.user.first_name
			comment.comment = request.POST['comment']
		comment.news = News.objects.get(id=int(request.path.split('/')[-1]))
		comment.save()
		return redirect(request.path)


class CreateNewsFormView(View):

	@staticmethod
	def get(request):
		if not request.user.groups.filter(name='verified').exists() and request.user.username != 'admin':
			raise PermissionDenied()
		news_form = NewsForm()
		return render(request, 'app_news/create_news.html', context={'news_form': news_form})

	@staticmethod
	def post(request):
		if not request.user.has_perm('app_news.can_add'):
			raise PermissionDenied()
		news_form = NewsForm(request.POST)
		if news_form.is_valid():
			news = News()
			news.title = news_form.cleaned_data['title']
			news.content = news_form.cleaned_data['content']
			news.tag = news_form.cleaned_data['tag']
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
		if not request.user.has_perm('app_news.can_published'):
			raise PermissionDenied()
		news = News.objects.get(id=news_id)
		news_form = UpdateNewsForm(request.POST, instance=news)
		if news_form.is_valid():
			news.save()
		return HttpResponseRedirect('/')
