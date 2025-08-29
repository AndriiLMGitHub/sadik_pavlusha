from django.shortcuts import render
from .models import GalleryPhoto


def index(request):
    photos = GalleryPhoto.objects.all().order_by('-created_at')
    return render(request, 'app/sadik.html', {
        'photos': photos
    })
