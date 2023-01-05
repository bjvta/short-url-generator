"""HeyURL Services module"""

from heyurl.exceptions import ExistingUrlException, InvalidURLException
import random
import string
import re
from heyurl.models import Url


class CreateUrlService:
    def __init__(self, original_url):
        self.original_url = original_url

    def call(self):
        ValidateUrlFormatService.call(self.original_url)
        ValidateUniqueOriginalUrl(self.original_url).call()
        short_url = CreateShortUrlService(self.original_url).call()
        url = Url.objects.create(short_url=short_url, original_url=self.original_url)
        return url



class CreateShortUrlService:
    def __init__(self, original_url):
        self.original_url = original_url

    def call(self):
        while True:
            short_url =''.join(random.choices(string.ascii_letters + string.digits, k=5))
            try:
                Url.objects.get(short_url=short_url)
            except Url.DoesNotExist:
                return short_url


class ValidateUniqueOriginalUrl:
    def __init__(self, original_url):
        self.original_url = original_url

    def call(self):
        try:
            Url.objects.get(original_url=self.original_url)
            raise ExistingUrlException
        except Url.DoesNotExist:
            return True


class ValidateUrlFormatService:
    @staticmethod
    def call(url):
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        if re.match(url_pattern, url) is None:
            raise InvalidURLException
        return True
