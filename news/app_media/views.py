from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm


def upload_file(request):
	if request.method == 'POST':
		upload_file_form = UploadFileForm(request.POST, request.FILES)
		if upload_file_form.is_valid():
			file = request.FILES['file']
			list_z = ['Это', 'слово', 'нельзя', 'использовать']
			for word in list_z:
				if word in upload_file_form.cleaned_data.get('file').read().decode('utf-8'):
					return HttpResponse(content='Файл не прошел проверку', status=500)

			return HttpResponse(content='It`s OK', status=200)
	else:
		upload_file_form = UploadFileForm()
	return render(request, 'app_media/upload_file.html', {'upload_file_form': upload_file_form})
