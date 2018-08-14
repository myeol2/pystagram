from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
from .forms import PhotoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def detail(request, pk):

    photo = get_object_or_404(Photo,pk=pk)

    #photo class has image field(variable), and ImageFile object has url.
    msg = ('<p>Let me show you No. {pk} photo. </p>'.format(pk=photo.pk),
            '<p>address is {url}</p>'.format(url=photo.image.url),
            '<p><img src="{url}" /></p>'.format(url=photo.image.url)
    )
        
    return HttpResponse('\n'.join(msg))

@login_required
def create(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit="False")
            obj.user = request.user
            obj.save()
            return redirect(obj)

    # ctx= context(템플릿 맥락 요소), template에 전달할 내용
    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)
