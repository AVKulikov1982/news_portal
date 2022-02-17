from django.urls import path

from .views import ItemsListView, upload_price_file, upload_file


urlpatterns = [
	path('items/', ItemsListView.as_view(), name='items_list'),
	path('items/upload_file/', upload_file, name='app_media/document'),
	path('items/upload_price_file/', upload_price_file, name='upload_price_file')
]