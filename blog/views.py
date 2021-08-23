from django.shortcuts import render, get_list_or_404
from .models import Post
from django.conf import settings

def index(request):
    type_list = Post.objects.get(id=12).TypeOfPicture

    context = {'media_url':settings.MEDIA_URL, 'type_list': type_list}
    return render(request, "blog/presentation.html", context)

def image(request, picture_type):

    image_list = get_list_or_404(Post, type_image=picture_type)
    type_list = Post.objects.get(id=12).TypeOfPicture

    context = {'image_list': image_list, 'media_url':settings.MEDIA_URL, 'type_list': type_list}
    return render(request, "blog/home.html", context)
