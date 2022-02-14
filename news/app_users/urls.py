from django.urls import path

from app_users.views import UserLoginView, UserLogoutView, register, account,\
	AppModeratorListView, UpdateModeratorView, AppVerifiedListView, UpdateVerifiedView

urlpatterns = [
	path('user/login', UserLoginView.as_view(), name='login'),
	path('user/logout', UserLogoutView.as_view(), name='logout'),
	path('user/registration', register, name='registration'),
	path('user/account', account, name='account'),
	path('user/add_moderator', AppModeratorListView.as_view(), name='moderators_list'),
	path('user/add_moderator/<int:user_id>', UpdateModeratorView.as_view(), name='moderators_detail'),
	path('user/add_verified', AppVerifiedListView.as_view(), name='verified_list'),
	path('user/add_verified/<int:user_id>', UpdateVerifiedView.as_view(), name='verified_detail'),
]
