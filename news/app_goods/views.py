from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Items
from app_media.forms import DocumentForm
from django.http import HttpResponse


class ItemsListView(generic.ListView):
	model = Items
	template_name = 'app_goods/items_list.html'
	queryset = Items.objects.all()
	context_object_name = 'items_list'


def upload_price_file(request):
	c_update = 0
	new_articles = []
	c_articles = len(Items.objects.all())
	if request.method == 'POST':
		upload_file_form = UploadFileForm(request.POST, request.FILES)
		if upload_file_form.is_valid():
			list_data = request.FILES['file'].read().decode('utf-8').split('\n')
			for item in list_data:
				title, price = item.split(':')
				if Items.objects.filter(title=title):
					Items.objects.filter(title=title).update(price=price)
					c_update += 1
				else:
					Items.objects.create(title=title, price=price)
					new_articles.append(title)
			return HttpResponse(content=f'It`s OK; '
										f'количество обновленных записей - {c_update}; '
										f'количество не обновленных записей - {c_articles - c_update}; '
										f'новые товары - {new_articles}; ', status=200)
	else:
		upload_file_form = UploadFileForm()
	return render(request, 'app_goods/upload_price_file.html', {'upload_file_form': upload_file_form})


def upload_file(request):

	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = DocumentForm()
	return render(request, 'app_media/document.html', {'form': form})
