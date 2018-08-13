from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
# Create your views here.

def detail(request, pk):

    photo = get_object_or_404(Photo,pk=pk)

    #photo class has image field(variable), and ImageFile object has url.
    msg = ('<p>Let me show you No. {pk} photo. </p>'.format(pk=photo.pk),
            '<p>address is {url}</p>'.format(url=photo.image.url),
            '<p><img src="{url}" /></p>'.format(url=photo.image.url)
    )
        
    return HttpResponse('\n'.join(msg))
