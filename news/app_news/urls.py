from django.urls import path

from .views import NewsListView, NewsDetailView, CreateNewsFormView, UpdateNewsView, home_page, SelectNewsListView, \
	UserLoginView, UserLogoutView, logout

urlpatterns = [
	path('', home_page, name='home'),
	path('user/login', UserLoginView.as_view(), name='login'),
	path('user/logout', UserLogoutView.as_view(), name='logout'),
	path('logout/', logout, name='logout'),
	path('create_news/', CreateNewsFormView.as_view()),
	path('select_news/', SelectNewsListView.as_view()),
	path('update_news/<int:news_id>', UpdateNewsView.as_view()),
	path('news/', NewsListView.as_view(), name='news_list'),
	path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]
