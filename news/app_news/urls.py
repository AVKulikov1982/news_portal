from django.urls import path

from .views import NewsListView, NewsDetailView, CreateNewsFormView, UpdateNewsView, home_page, SelectNewsListView


urlpatterns = [
	path('', home_page, name='home'),
	path('create_news/', CreateNewsFormView.as_view()),
	path('select_news/', SelectNewsListView.as_view()),
	path('update_news/<int:news_id>', UpdateNewsView.as_view()),
	path('news', NewsListView.as_view(), name='news_list'),
	path('news/', NewsListView.as_view(), name='news_list'),
	path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]
