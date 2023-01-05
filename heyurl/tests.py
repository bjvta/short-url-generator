from heyurl.exceptions import ExistingUrlException, InvalidURLException
from heyurl.services import CreateShortUrlService, CreateUrlService, ValidateUniqueOriginalUrl, ValidateUrlFormatService
from django.test import TestCase
from django.urls import reverse
from .models import Url

class IndexTests(TestCase):
    def test_no_urls(self):
        """
        If no URLs exist, an appropriate message is displayed
        """
        # response = self.client.get(reverse('index'))

    def test_submitting_new_url_failure(self):
        """
        When submitting an invalid URL, an error is returned to the user
        """
        # response = self.client.get(reverse('store'))

    def test_submitting_new_url_success(self):
        """
        When submitting a valid URL, a success message is displayed
        """
        # response = self.client.get(reverse('store'))

    def test_visiting_short_url_missing(self):
        """
        If short URL does not exist, custom 404 page is displayed
        """
        # response = self.client.get(reverse('u/dne'))

    def test_visiting_short_url(self):
        """
        If short URL exists, stats logged and redirected to original URL
        """
        # response = self.client.get(reverse('u/dne'))


class CreateUrlServiceTest(TestCase):
    def test_valid_one(self):
        given_url = 'http://google.com'
        before_save_count = Url.objects.count()
        expected_result = CreateUrlService(given_url).call()
        after_save_count = Url.objects.count()
        self.assertIsInstance(expected_result, Url)
        self.assertNotEqual(before_save_count, after_save_count)

    def test_invalid_one(self):
        given_url = 'asdfasdfasdf'
        with self.assertRaises(InvalidURLException):
            CreateUrlService(given_url).call()

    def test_existing_url(self):
        given_url = 'http://google.com'
        Url(short_url='asdfg',original_url=given_url).save()
        with self.assertRaises(ExistingUrlException):
            CreateUrlService(given_url).call()


class CreateShortUrlTest(TestCase):
    def test_given_one(self):
        given_url = 'http://google.com'
        result = CreateShortUrlService(given_url).call()
        self.assertEqual(len(result), 5)


class ValidateUniqueOriginalUrlTest(TestCase):
    def test_existing_url(self):
        given_url = 'http://google.com'
        Url(short_url='asdfg',original_url=given_url).save()
        with self.assertRaises(ExistingUrlException):
            ValidateUniqueOriginalUrl(given_url).call()


    def test_not_existing(self):
        given_url = 'http://google.com'
        result = ValidateUniqueOriginalUrl(given_url).call()
        self.assertTrue(result)


class ValidateUrlFormatTest(TestCase):
    def test_invalid(self):
        given_url = 'http//google.com'
        with self.assertRaises(InvalidURLException):
            ValidateUrlFormatService.call(given_url)

    def test_valid(self):
        given_url = 'http://google.com'
        result = ValidateUrlFormatService.call(given_url)
        self.assertTrue(result)

