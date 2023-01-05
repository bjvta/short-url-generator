from heyurl.services import CreateShortUrlService, CreateUrlService
from heyurl.exceptions import ExistingUrlException, InvalidURLException
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Click, Url

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
    browser = request.user_agent.browser.family
    platform = request.user_agent.os.family
    url = get_object_or_404(Url, short_url=short_url)
    Click.objects.create(url=url, browser=browser, platform=platform)
    url.clicks = url.clicks + 1
    url.save()
    return HttpResponse("You're looking at url %s" % short_url)


def short_url_stats(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)

    context = {url : url}
    return render(request, 'heyurl/stats.html', context)
