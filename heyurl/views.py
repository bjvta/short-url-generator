from heyurl.services import CreateShortUrlService, CreateUrlService
from heyurl.exceptions import ExistingUrlException, InvalidURLException
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Url

def index(request):
    urls = Url.objects.order_by('-created_at')
    context = {'urls': urls}
    return render(request, 'heyurl/index.html', context)

def store(request):
    try:
        original_url = request.POST.get('original_url')
        CreateUrlService(original_url).call()
        return HttpResponseRedirect(reverse('index'))
    except ExistingUrlException:
        print('this here')
        return HttpResponse('The original URL already exists')
    except InvalidURLException:
        print('this here')
        return HttpResponse('The URL given is invalid')


def short_url(request, short_url):
    # FIXME: Do the logging to the db of the click with the user agent and browser
    return HttpResponse("You're looking at url %s" % short_url)
