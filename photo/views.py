from django.shortcuts import render

from .models import Photo


def photo_list_view(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos':photos})


def photo_create_view(request):
    pass


def photo_update_view(request):
    pass


def photo_delete_view(request):
    pass
