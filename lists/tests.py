from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

# class SmokeTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1+1,3)


class HomePageTest(TestCase):

    # These two test method were replaced by one with two lines.
    #
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     # Replace these two lines with one line.
    #     # request = HttpRequest()
    #     # response = home_page(request)
    #     response = self.client.get('/')
    #     #
    #     html = response.content.decode('utf8')
    #     # print(repr(html)) # to check what charactors are actual in it.
    #     self.assertTrue(html.startswith('<!DOCTYPE html>\n<html'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     #
    #     # Replace these two lines with one line.
    #     # expected_html = render_to_string('home.html')
    #     # self.assertEqual(html, expected_html)
    #     self.assertTemplateUsed(response, 'home.html')
    #     # self.assertTemplateUsed(response, 'wrong.html') # for error messages

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

